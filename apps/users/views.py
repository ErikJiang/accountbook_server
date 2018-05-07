from django.shortcuts import render
from apps.users.models import CustomUser
from apps.users.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class UsersViewSet(viewsets.ModelViewSet):
  queryset = CustomUser.objects.all()
  serializer_class = UserSerializer
  permission_classes = (IsAuthenticated,)