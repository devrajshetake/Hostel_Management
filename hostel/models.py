import email
from django import forms
from django.db import models
from django.forms import CharField, EmailField, NumberInput,TimeInput,TimeField,DateField , ImageField
from django.contrib.auth.models import User
from django.utils.html import mark_safe
YEAR_CHOICES =[
    ('FE','FE'),
    ('SE', 'SE'),
    ('TE','TE'),
    ('BE','BE'),    
]
class contactUs(models.Model):
    name=models.CharField(max_length=50)
    email_id=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return self.name

class VisitorDetails(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    room=models.IntegerField()
    phone=models.IntegerField()
    intime=models.TimeField()
    outtime=models.TimeField()
    relation=models.TextField()  
    def __str__(self):
        return self.fname

class studentDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    fname=models.CharField(max_length=30, null=True)
    lname=models.CharField(max_length=30,default= " ",null=True)
    branch=models.CharField(max_length=30,null=True)
    year= models.CharField(max_length=6, choices=YEAR_CHOICES, default='FE',null=True)
    # year=models.CharField(max_length=30,null=True)
    reg=models.CharField(max_length=30,null=True)
    roll=models.IntegerField(null=True)
    dob=models.DateField(null=True)
    mob=models.CharField(max_length=100,null=True)
    mob1=models.IntegerField(null=True)
    mob2=models.IntegerField(null=True)
    email1=models.EmailField(null=True)
    email2=models.EmailField(null=True)
    hometown=models.CharField(max_length=20,null=True)
    state=models.CharField(max_length=30,null=True)
    caste=models.CharField(max_length=30,null=True)
    nation=models.CharField(max_length=30,null=True)
    aadhar=models.IntegerField(null=True)
    pan=models.CharField(max_length=8,null=True)
    blood=models.CharField(max_length=10,null=True)
    allergy=models.CharField(max_length=30,null=True)
    guard=models.CharField(max_length=30,null=True)
    gaddress=models.CharField(max_length=100,null=True)
    gnumber=models.IntegerField(null=True)
    rel=models.CharField(max_length=30,null=True)
    sphoto=models.ImageField(null=True, upload_to='images/')
    aphoto=models.ImageField(null=True, upload_to='images/')
    svaccine=models.ImageField(null=True, upload_to='images/')
    certi=models.ImageField(null=True, upload_to='images/')
    def __str__(self):
        return self.fname 



# class Model1(models.Model):
#     sphoto = models.ImageField(upload_to='images/')

#     def image_tag(self):
#         return mark_safe('<img src="/images/%s" width="150" height="150" />' % (self.sphoto))

#     image_tag.short_description = 'Image'

