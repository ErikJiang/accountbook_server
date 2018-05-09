from django.shortcuts import render
from apps.categorys.models import Categorys
from apps.categorys.serializers import CategorySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class CategorysViewSet(viewsets.ModelViewSet):
    queryset = Categorys.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, )

    # 创建时默认设置用户关联关系
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # 更新时再次更新用户关联关系
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
