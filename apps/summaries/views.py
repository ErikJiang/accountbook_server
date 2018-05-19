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
        
        ---
        
        ## request:

        |参数名|描述|请求类型|参数类型|备注|
        |:----:|:----:|:----:|:----:|:----:|
        | time_type | 时间类型 | query | string | `YEAR` or `MONTH` |  
        | time_value | 时间值 | query | string |  `YYYY` or `YYYY-MM`|
            
        ## response:
        ``` json
        {
            "time": "统计时间",
            "income_amount": "收入数额",
            "outgo_amount": "支出数额",
            "balance_amount": "结余数额"
        }
        """
        query = self.get_queryset()

        result = query.values('bill_type').annotate(
            amount_sum=Sum('amount')).order_by()
        print(result.query)
        print(result)

        try:
            income_amount = result.get(bill_type=1)['amount_sum']
        except Bills.DoesNotExist:
            income_amount = 0
        try:
            outgo_amount = result.get(bill_type=0)['amount_sum']
        except Bills.DoesNotExist:
            outgo_amount = 0

        res_dict = {
            "time": request.query_params.get('time_value'),
            "income_amount": income_amount,
            "outgo_amount": outgo_amount,
            "balance_amount": income_amount - outgo_amount
        }
        return Response(data=res_dict, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False)
    def linechart(self, request):
        """
        折线图

        ---
        
        ## request:

        |参数名|描述|请求类型|参数类型|备注|
        |:----:|:----:|:----:|:----:|:----:|
        | time_type | 时间类型 | query | string | `YEAR` or `MONTH` |  
        | time_value | 时间值 | query | string |  `YYYY` or `YYYY-MM`|
            
        ## response:
        ``` json
        {
            "income_data": [
                {
                    "date": "YYYY-MM or YYYY-MM-DD",
                    "amount": "金额"
                }
            ],
            "outgo_data": [
                {
                    "date": "YYYY-MM or YYYY-MM-DD",
                    "amount": "金额"
                }
            ]
        }
        """
        time_type = self.request.query_params.get('time_type')
        queryset = self.get_queryset()

        if time_type == 'YEAR':
            # todo bill_type(income or outgo)
            year_stat = queryset.extra({
                'time': "DATE_FORMAT(record_date,'%%Y-%%m')"
            }).values('time').annotate(total_amount=Sum('amount')).order_by()
            print(year_stat.query)
            print(year_stat)

        if time_type == 'MONTH':
            # todo bill_type(income or outgo)
            month_stat = queryset.extra({
                'time': "DATE_FORMAT(record_date,'%%Y-%%m-%%d')"
            }).values('time').annotate(total_amount=Sum('amount')).order_by()
            print(month_stat.query)
            print(month_stat)
        
        return Response(status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False)
    def ringchart(self, request):
        """
        环状图

        ---
        
        ## request:

        |参数名|描述|请求类型|参数类型|备注|
        |:----:|:----:|:----:|:----:|:----:|
        | time_type | 时间类型 | query | string | `YEAR` or `MONTH` |  
        | time_value | 时间值 | query | string |  `YYYY` or `YYYY-MM`|
            
        ## response:
        ``` json
        {
            "income_data": [
                {
                    "category": "类别",
                    "amount": "金额"
                }
            ],
            "outgo_data": [
                {
                    "category": "类别",
                    "amount": "金额"
                }
            ]
        }
        """
        queryset = self.get_queryset()

        category_stat = queryset.values('category').annotate(
            amount_sum=Sum('amount')).order_by()
        print(category_stat.query)
        print(category_stat)

        # todo
        return Response(status=status.HTTP_200_OK)
