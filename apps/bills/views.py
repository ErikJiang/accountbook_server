from django.shortcuts import render
from apps.bills.models import Bills
from apps.bills.serializers import BillSerializer

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# 过滤器
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from apps.bills.filters import BillsFilter

from rest_framework.decorators import action
from rest_framework.response import Response

from apps.bills.schemas import BillSchema

import logging
logger = logging.getLogger(__name__)

# 分页设置
class ResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class BillsViewSet(viewsets.ModelViewSet):
    serializer_class = BillSerializer
    pagination_class = ResultsSetPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = BillsFilter
    ordering_fields = ('amount', 'record_date')
    schema = BillSchema()

    # 覆写查询集，仅查询当前用户下的账目数据
    def get_queryset(self):
        return Bills.objects.filter(user=self.request.user)

    # 创建时默认设置用户关联关系
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # 更新时再次更新用户关联关系
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=['patch'], detail=False)
    def batch_del(self, request):

        if 'bill_ids' not in self.request.data:
            content = {'msg': 'request param bill_ids is not exist.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        
        bill_ids = self.request.data.get('bill_ids')
        if not isinstance(bill_ids, list):
            content = {'msg': 'request param bill_ids is invalid type.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        
        bills_data = Bills.objects.filter(pk__in=bill_ids)

        # todo update

        serializer = self.get_serializer(bills_data, many=True)
        return Response(serializer.data)
        