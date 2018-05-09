from rest_framework import serializers
from apps.bills.models import Bills
from apps.categorys.serializers import CategorySerializer

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = ('id', 'user', 'category', 'bill_type', 'amount', 'remarks', 'record_date',)
        read_only_fields = ('user',)

    # 覆写序列化表现: 展示category类别名称
    def to_representation(self, instance):
        representation = super(BillSerializer, self).to_representation(instance)
        category_data = CategorySerializer(instance.category).data
        representation['category'] = category_data['name']
        return representation
