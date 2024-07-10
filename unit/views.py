from rest_framework import viewsets
from .models import Unit, InvoiceDetails
from .serializers import UnitSerializer, InvoiceDetailsSerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class InvoiceDetailsViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetails.objects.all()
    serializer_class = InvoiceDetailsSerializer
