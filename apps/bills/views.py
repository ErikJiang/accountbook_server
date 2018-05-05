from django.shortcuts import render
from apps.bills.models import Bills
from apps.bills.serializers import BillSerializer

from rest_framework import viewsets
# Create your views here.

class BillsViewSet(viewsets.ModelViewSet):
    queryset = Bills.objects.all()
    serializer_class = BillSerializer
