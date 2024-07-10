from django.db import models


class Unit(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=225, )
    objects = models.manager


class InvoiceDetails(models.Model):
    lineno = models.IntegerField()
    product_name = models.CharField(max_length=225)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.DecimalField(decimal_places=2, max_digits=10)
    total = models.DecimalField(decimal_places=2, max_digits=10)
    expiryDate = models.DateTimeField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="invoices")
    objects = models.manager
