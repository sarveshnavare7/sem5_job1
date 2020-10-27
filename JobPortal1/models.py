from django.db import models

class sqlserverconn(models.Model):
    GSTNO= models.IntegerField()
    CompanyName= models.CharField(max_length=100)
    Locality= models.CharField(max_length=100)
    City= models.CharField(max_length=100)
    State= models.CharField(max_length=100)

class applicant(models.Model):
    jaadharnumber= models.IntegerField()
    jfname= models.CharField(max_length=20)
    jlname= models.CharField(max_length=20)
    jcity= models.CharField(max_length=20)
    jstate= models.CharField(max_length=20)
    jemail= models.CharField(max_length=30)
    jage= models.IntegerField()
