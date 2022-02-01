from django.db import models
from django.db.models.fields import CharField
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField







# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    email_add=models.EmailField(max_length=264)
    Telephone=PhoneNumberField(max_length=128,default='')
    country =CountryField(max_length=264,blank_label='(select country)',default='')
    budget=MoneyField(max_digits=14, decimal_places=2, default_currency='USD',default=1000,null=True)
    
    project=models.CharField(max_length=264,default='')
    option=models.CharField(max_length=264,default='')
    
    seo_options=models.TextField()
    digital_options=models.TextField()
    
    homepage=models.IntegerField(default=1)
    innerpages=models.IntegerField(default=1)
    
    html_options=models.CharField(max_length=264,default='')
    html_development_notes=models.CharField(max_length=264,default='')
    
    cms_options=models.CharField(max_length=264,default='')
    cms_development_notes=models.CharField(max_length=264,default='')
    
    frontend_options=models.CharField(max_length=264,default='')
    frontend_development_notes=models.CharField(max_length=264,default='')
    
    ecom_options=models.CharField(max_length=264,default='')
    ecom_development_notes=models.CharField(max_length=264,default='')

class Job(models.Model):
    first_name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    email_add=models.EmailField(max_length=264)
    Mobile=PhoneNumberField(max_length=128,default='')
    Experience=models.TextField()
    Apply_for=models.CharField(max_length=128)
    


    


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    def __str__(self):
       return self.email





   



    
   