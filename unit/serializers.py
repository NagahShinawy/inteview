from rest_framework import serializers
from .models import Unit, InvoiceDetails


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['pk', 'number', 'name']


class InvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetails
        fields = [
            'id',
            'lineno',
            'product_name',
            'price',
            'quantity',
            'total',
            'expiryDate',
            'unit'
        ]
