from django.db import models
class tbl_login(models.Model):
    username=models.CharField(max_length=50)
    fisrtname=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    class Meta:
        db_table='tbl_login'

# Create your models here.
