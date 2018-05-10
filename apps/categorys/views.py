from django.db.models import Q
from apps.categorys.models import Categorys
from apps.categorys.serializers import CategorySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class CategorysViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, )

    # 当前用户自定义类型或默认类型
    def get_queryset(self):
        return Categorys.objects.filter(
            Q(user=self.request.user) | Q(is_default=True))

    # 创建时默认设置用户关联关系
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # 更新时再次更新用户关联关系
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
