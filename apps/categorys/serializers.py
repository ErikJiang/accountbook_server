from rest_framework import serializers
from apps.categorys.models import Categorys

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorys
        fields = ('id', 'user_id', 'parent_id', 'is_default', 'bill_type', 'name')