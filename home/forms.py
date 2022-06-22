from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import student_info
from django.core import validators

class studentr(forms.ModelForm):
    class meta:
        Model = student_info
        fields = ["Roll_no","first_name","last_name","dob","gender","contect","email","course","address"]