from django.urls import reverse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_csv.parsers import CSVParser
from rest_framework_csv.renderers import CSVRenderer
from apps.bills.models import Bills
from apps.bills.serializers import BillSerializer


class UtilViewSet(viewsets.GenericViewSet):
    queryset = Bills.objects.all()
    parser_classes = (CSVParser,) + tuple(api_settings.DEFAULT_PARSER_CLASSES)
    renderer_classes = (CSVRenderer,) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    serializer_class = BillSerializer

    def get_renderer_context(self):
        context = super(UtilViewSet, self).get_renderer_context()
        context['header'] = (self.request.GET('fields').split(',')
                             if 'fields' in self.request.GET else None)
        return context

    @action(methods=['POST'], detail=False)
    def bulk_upload(self, request, *args, **kwargs):
        """
        Try out this view with the following curl command:
        ``` bash
        curl -X POST http://localhost:8000/talks/bulk_upload/ \
            -d "category,bill_type,amount,remarks,record_date
                1,INCOME,1000,test_remark,2017-12-03
                2,INCOME,2000,test_remark,2018-11-03
                3,OUTGO,1500,test_remark,2018-11-03" \
            -H "Content-type: text/csv" \
            -H "Accept: text/csv"
        ```
        """
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_303_SEE_OTHER,
            headers={'Location': reverse('talk-list')})

