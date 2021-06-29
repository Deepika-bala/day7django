from django.db import models

# Create your models here.
class Request(models.Model):
    req_id = models.AutoField(db_column='req_id', primary_key=True)
    f_name = models.CharField(max_length=30, null=False)
    l_name = models.CharField(max_length=30, null=False)
    user_dob = models.CharField(max_length=20,null=False)
    user_gender = models.CharField(max_length=30, null=False)
    user_nationality = models.CharField(max_length=30, null=False)
    user_city = models.CharField(max_length=30, null=False)
    user_state = models.CharField(max_length=30, null=False)
    user_pincode =models.CharField(max_length=6, null=False)
    user_qualification =models.CharField(max_length=30, null=False)
    user_salary = models.IntegerField(null=False)
    user_pannumber = models.CharField(max_length=10, null=False)

