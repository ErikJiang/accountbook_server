from rest_framework import serializers
from apps.users.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('id', 'email', 'username', 'first_name', 'last_name', 'last_login')
