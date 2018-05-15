from rest_framework import serializers

class SummariesSerializer(serializers.Serializer):
  time_type = serializers.ChoiceField(choices=['YEAR', 'MONTH'], required=True)
  time_value = serializers.CharField(required=True)