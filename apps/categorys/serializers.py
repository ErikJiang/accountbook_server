from rest_framework import serializers
from apps.categorys.fields import EnumField
from apps.categorys.models import BillType, Categorys


class CategorySerializer(serializers.ModelSerializer):
    bill_type = EnumField(enum=BillType)

    class Meta:
        model = Categorys
        fields = ('id', 'user', 'parent', 'is_default', 'bill_type', 'name')
        read_only_fields = ('user', 'is_default')
