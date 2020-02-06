from django.db import models
from django.utils import timezone

# Create your models here.


class stock(models.Model):
    materialno=models.CharField(unique=True,max_length=50)
    nomenclature = models.CharField(max_length=50)
    quantityrecieved = models.IntegerField()
    wtratio = models.IntegerField()
    subdepot = models.IntegerField()


class issueregister(models.Model):
    materialno=models.CharField(max_length=50)
    nomenclature = models.CharField(max_length=50)
    quantityheld = models.IntegerField()
    issueqty = models.IntegerField()
    subdepot = models.IntegerField()
    unit = models.TextField()
    issuedate = models.DateField(null=True)


class loadchart(models.Model):
    unit= models.TextField(null=True)
    totalload = models.IntegerField(blank=True,null=True)
    expdate = models.DateField(blank=True,null=True)
    sd1 = models.IntegerField(blank=True,null=True)
    d1 = models.DateField(blank=True,null=True)
    sd2 = models.IntegerField(blank=True,null=True)
    d2 = models.DateField(blank=True,null=True)
    sd3 = models.IntegerField(blank=True,null=True)
    d3 = models.DateField(blank=True,null=True)
    sd4 = models.IntegerField(blank=True,null=True)
    d4 = models.DateField(blank=True,null=True)

