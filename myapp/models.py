import email
from email.policy import default
from statistics import mode
from django.db import models
from sqlalchemy import false

# # Create your models here.
# class Student(models.Model):
#     Firstname=models.CharField(max_length=50)
#     lastname=models.CharField(max_length=50)
#     email=models.EmailField(max_length=50)
#     contact=models.BigIntegerField()

    

class file_only(models.Model):
    id = models.AutoField(primary_key=True)
    # file_name = models.CharField(max_length=255)
    my_file1 = models.FileField(upload_to='')
    my_file2= models.FileField(upload_to='')
    my_file3 = models.FileField(upload_to='')
    my_file4 = models.FileField(upload_to='')
    
# Create your models here.
class User(models.Model):
    # Username=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)
    is_active=models.CharField(max_length=50,default=0)
    user_type=models.CharField(max_length=50,default=0)
    
class User5(models.Model):
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)
    
class User1(models.Model):
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)
    
class User6(models.Model):
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)

class User7(models.Model):
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)
    
class User8(models.Model):
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)    


class User9(models.Model):
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)
    
class User10(models.Model):
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)
   
   
class User11(models.Model):
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)   
    
   
class User12(models.Model):
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)   
    
    
class personalinfo(models.Model):
    Fulladress=models.CharField(max_length=50)
    District=models.CharField(max_length=50)
    Administration=models.CharField(max_length=50)
    Office=models.CharField(max_length=50)
    Ministry=models.CharField(max_length=50)
    Area=models.CharField(max_length=50)
    Atonomous=models.CharField(max_length=50)
    Disability=models.CharField(max_length=50)
    Family=models.CharField(max_length=50)
    Mothername=models.CharField(max_length=50)
    Telephone=models.CharField(max_length=12)
    Frname=models.CharField(max_length=50)
    Teleph=models.CharField(max_length=50)
    Partner=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    Directorate=models.CharField(max_length=50)
    Ministryy=models.CharField(max_length=50)
    Checkbox1=models.CharField(max_length=10)
    Checkbox2=models.CharField(max_length=10)
    Radio1=models.CharField(max_length=50,default=50)
    Radio2=models.CharField(max_length=50,default=50)
    Radio3=models.CharField(max_length=50,default=50)
    Date1=models.DateField(default=false)
    Date2=models.DateField(default=false)
    file1=models.FileField(max_length=250)
    file2=models.FileField(max_length=250)
    file3=models.FileField(max_length=250)
    file4=models.FileField(max_length=250)
    Apartment=models.CharField(max_length=50,default=50)


    
#    my_file =models.FileField(uplode_to='')
    
    # def __str__(self):
    #     return self.file_name
    
    def add(self, *args, **kwargs):
        super(personalinfo , self).add(*args, **kwargs)
          