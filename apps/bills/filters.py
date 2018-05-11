from django_filters import rest_framework as filters
from apps.bills.models import Bills

class BillsFilter(filters.FilterSet):
    """
    账目过滤器
    """
    bill_type = filters.NumberFilter(name='bill_type')
    min_amount = filters.NumberFilter(name='amount', lookup_expr='gte')
    max_amount = filters.NumberFilter(name='amount', lookup_expr='lte')
    start_date = filters.DateFilter(name='record_date', lookup_expr='gte')
    end_date = filters.DateFilter(name='record_date', lookup_expr='lte')
    remarks = filters.CharFilter(name='remarks', lookup_expr='icontains')

    class Meta:
        model = Bills
        fields = (
            'category',
            'bill_type',
            'min_amount',
            'max_amount',
            'start_date',
            'end_date',
            'remarks',
        )
