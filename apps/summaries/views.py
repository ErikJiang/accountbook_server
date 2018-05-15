from rest_framework.decorators import action
from rest_framework.schemas import AutoSchema
from rest_framework.response import Response
from rest_framework import viewsets, status
from coreapi import Field, Link, document
from django.db.models import Sum
import coreschema
from apps.summaries.serializers import SummariesSerializer
from apps.bills.serializers import BillSerializer
from apps.bills.models import Bills

# request: {
#    date: 'YYYY or YYYY-MM'
# }

# 概要信息
# response: {
#    date: 'YYYY or YYYY-MM',
#    income_amount: '收入金额',
#    outgo_amount: '支出金额',
#    balance_amount: '结余金额'
# }

# 折线信息
# response: {
#    income_data: [
#        {
#           date: 'YYYY-MM or YYYY-MM-DD',
#           amount: '金额'
#        }
#    ],
#    outgo_data: [
#        {
#           date: 'YYYY-MM or YYYY-MM-DD',
#           amount: '金额'
#        }
#     ]
# }

# 环状信息
# response: {
#    income_data: [
#        {
#           category: '类别',
#           amount: '金额'
#        }
#    ],
#    outgo_data: [
#        {
#           category: '类别',
#           amount: '金额'
#        }
#     ]
# }


class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):
        link = super().get_link(path, method, base_url)
        fields = [
            Field(
                'time_type',
                location='query',
                required=True,
                schema=coreschema.Enum(enum=['year', 'month'])),
            Field(
                'time_value',
                location='query',
                required=True,
                schema=coreschema.String()),
        ]
        fields = tuple(fields)
        link = Link(
            url=link.url,
            action=link.action,
            encoding=link.encoding,
            fields=fields,
            description=link.description)
        document.Link()
        return link


class SummariesViewSet(viewsets.GenericViewSet):
    schema = CustomAutoSchema()

    def get_queryset(self):
        serializer = SummariesSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        time_type = self.request.query_params.get('time_type')
        time_value = self.request.query_params.get('time_value')
        if time_type == 'YEAR':
            return Bills.objects.filter(
                record_date__year=time_value, user=self.request.user)
        if time_type == 'MONTH':
            time_value = time_value.split('-', 1)
            return Bills.objects.filter(
                record_date__year=time_value[0],
                record_date__month=time_value[1],
                user=self.request.user)

    @action(methods=['GET'], detail=False)
    def info(self, request):
        """
        概要信息
        """
        query = self.get_queryset()

        result = query.values('bill_type').annotate(amount_sum=Sum('amount'))
        print(result)
        # todo
        res_dict = {
            "time": request.query_params.get('time_value'),
            "income_amount": '收入金额',
            "outgo_amount": '支出金额',
            "balance_amount": '结余金额'
        }
        return Response(data=res_dict, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False)
    def linechart(self, request):
        """
        折线图
        """
        serializer = SummariesSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        # todo
        return Response(status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False)
    def ringchart(self, request):
        """
        环状图
        """
        serializer = SummariesSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        # todo
        return Response(status=status.HTTP_200_OK)
