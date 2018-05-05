from rest_framework import serializers
from apps.bills.models import Bills

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = ('user_id', 'category_id', 'bill_type', 'amount', 'remarks', 'record_date')