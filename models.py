from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class student_info(models.Model):
    Roll_no = models.AutoField(primary_key=True,)
    first_name = models.CharField(max_length=500)

    last_name = models.CharField(max_length=50)
    dob = models.CharField( max_length=100)
    gender = models.CharField( max_length=50)
    contect =models.CharField(max_length=50)
    email = models.EmailField(max_length=300)
    
    course = models.CharField(max_length=200)
    address = models.CharField(max_length=400)

    def __str__(self):
        return self.first_name # show on admin page 
class meta:
    abstract=True
    
    
class name(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
        
    
class attendane(models.Model):
    student = models.OneToOneField(name,on_delete=models.CASCADE)
    
    attendane=models.CharField("this student in the class",default=False,max_length=300)
    
    
    # name = models.CharField(max_length=100)
    def name (self):
        return self.attendane