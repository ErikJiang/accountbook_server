from rest_framework.decorators import action
from rest_framework.schemas import AutoSchema
from rest_framework.response import Response
from rest_framework import viewsets, status
from coreapi import Field, Link, document
import coreschema

from apps.summaries.serializers import SummariesSerializer

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

    @action(methods=['GET'], detail=False)
    def info(self, request):
        """
        概要信息
        """
        serializer = SummariesSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        # todo
        return Response(status=status.HTTP_200_OK)

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
