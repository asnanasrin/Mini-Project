from django.db import models

# Create your models here.

class regmodel(models.Model):
    fname=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    phoneNumber=models.CharField(max_length=200,null=True)
    # gen=models.CharField(max_length=200,null=True)
    adrs=models.CharField(max_length=200,null=True)
    District=models.CharField(max_length=200,null=True)

class usermodel(models.Model):
    uname=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    upassword=models.CharField(max_length=200,null=True)
    phoneNumber=models.CharField(max_length=200,null=True)
    # gen=models.CharField(max_length=200,null=True)
    adrs=models.CharField(max_length=200,null=True)
    District=models.CharField(max_length=200,null=True)
    vid=models.CharField(max_length=200,null=True)


class casemodel(models.Model):
    caseid=models.CharField(max_length=200,null=True)
    casename=models.CharField(max_length=200,null=True)
    discription=models.CharField(max_length=200,null=True)
    location=models.CharField(max_length=200,null=True)
    vehicleno=models.CharField(max_length=200,null=True)
    uname=models.CharField(max_length=200,null=True)
    vehicleownerid=models.CharField(max_length=200,null=True)
    amount=models.CharField(max_length=200,null=True)
    date=models.CharField(max_length=200,null=True)

class rulemodel(models.Model):
    ruleid=models.CharField(max_length=200,null=True)
    rule=models.CharField(max_length=200,null=True)

class resultmodel(models.Model):
    vehicleno=models.CharField(max_length=200,null=True)
    # uname=models.CharField(max_length=200,null=True)
    
