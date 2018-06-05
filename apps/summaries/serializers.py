from rest_framework import serializers
from apps.categorys.serializers import CategorySerializer


class SummariesSerializer(serializers.Serializer):
    time_type = serializers.ChoiceField(
        choices=['YEAR', 'MONTH'], required=True)
    time_value = serializers.CharField(required=True)


class RingchartSerializer(serializers.Serializer):
    def to_internal_value(self, data):

        if not data:
            return []

        def data_handler(item):
            category_data = CategorySerializer(item['category']).data
            item['category'] = category_data['name']
            return item

        return map(data_handler, data)
