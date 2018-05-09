from rest_framework import serializers
from apps.categorys.models import Categorys

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorys
        fields = ('id', 'user', 'parent', 'is_default', 'bill_type', 'name')
        read_only_fields = ('user',)