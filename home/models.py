from django.db import models

# Create your models here.
class student_info(models.Model):
    Roll_no = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=500)

    last_name = models.CharField(max_length=50)
    dob = models.CharField( max_length=100)
    gender = models.CharField( max_length=50)
    contect =models.CharField(max_length=50)
    email = models.EmailField(max_length=300)
    
    course = models.CharField(max_length=200)
    address = models.CharField(max_length=400)

    def __str__(self):
        return self.first_name