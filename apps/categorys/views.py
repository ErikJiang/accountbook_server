from django.shortcuts import render
from apps.categorys.models import Categorys
from apps.categorys.serializers import CategorySerializer
from rest_framework import viewsets

# Create your views here.
class CategorysViewSet(viewsets.ModelViewSet):
    queryset = Categorys.objects.all()
    serializer_class = CategorySerializer