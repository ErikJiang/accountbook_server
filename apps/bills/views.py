from django.shortcuts import render
from apps.bills.models import Bills
from apps.bills.serializers import BillSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# 过滤器
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from apps.bills.filters import BillsFilter

# 分页设置
class ResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10

class BillsViewSet(viewsets.ModelViewSet):
    serializer_class = BillSerializer
    pagination_class = ResultsSetPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = BillsFilter
    ordering_fields = ('amount', 'record_date')

    # 覆写查询集，仅查询当前用户下的账目数据
    def get_queryset(self):
        return Bills.objects.filter(user=self.request.user)

    # 创建时默认设置用户关联关系
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # 更新时再次更新用户关联关系
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
