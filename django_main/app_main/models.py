from django.db import models

# Create your models here.

class Vendor(models.Model):
    VendorNo = models.CharField(max_length=255,primary_key=True)
    VendorName = models.CharField(max_length=500)
    Email = models.EmailField()
    Territory = models.CharField(max_length=255)
    IaAlertDays = models.IntegerField()

class PurchaseOrder(models.Model):
    PONO = models.CharField(max_length = 255,primary_key=True)
    VendorNo = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    ShipDate = models.DateField()
    Customer = models.CharField(max_length=255)
    IaSubmissionDate = models.DateField() 
    InspectionDate = models.DateField()