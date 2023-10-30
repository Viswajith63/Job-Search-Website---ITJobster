from django.db import models

class administrator(models.Model):
    adminname=models.EmailField(max_length=100)
    adminpass=models.CharField(max_length=25)

class user(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    age=models.IntegerField()
    phone=models.BigIntegerField()
    location=models.CharField(max_length=100)
    aadhar=models.BigIntegerField()
    password=models.CharField(max_length=100)


class company(models.Model):
    gstin=models.CharField(max_length=100,primary_key=True,unique=True)
    companyname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    contact=models.BigIntegerField()
    password=models.CharField(max_length=100)


