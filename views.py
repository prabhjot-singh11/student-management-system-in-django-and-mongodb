from django import forms
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate, login
from .models import student_info
from .models import attendane
from .forms import studentr
# import matplotlib.pyplot as plt
# import numpy as np

# Create your views here.
def index(request):
    # return HttpResponse("this is login page")
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
      
        myuser.save()


        messages.success(request,"your account hass succesfully made")

        return redirect("signin")

    else:
        print("account can not be created")








    # return HttpResponse("this is the service page")
    return render(request,'login.html')

def signin(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        
        
        user = authenticate(username=username,password = pass1)
        if user is not None:
            login(request,user)
            return render(request,"main.html")
            
        else:
            messages.error(request,"not a user")
        
    
    return render(request,"signin.html")   

def signout(request):
    return render(request,"index.html")


def add(request):
    return render(request,"main.html")


def add_student(request):
  if request.method == "POST":
    
 
    
    fname = request.POST.get("firstname")
    lname = request.POST.get("lsname")
    date = request.POST.get("dat")
    gender = request.POST.get("gender") 
    contect = request.POST.get("contect")
    email = request.POST.get("email")
    course = request.POST.get("course")
    address = request.POST.get("address")
    
    messages.success(request,"new student added into database")
    
    
    students= student_info(first_name = fname,last_name = lname,dob=date,gender =gender,contect =contect,  email = email,course =course,address=address )
    students.save()
    

  return render(request,"add.html")



def student_data(request):
    allstudents = student_info.objects.all()
    
    
    
    
    
    return render(request,"info.html",{'studentinfo' :allstudents})

def ex(request):
#  if request.method=="POST":
 
    students= student_info.objects.all()
    # students.delete()
    context = {
        "students":students
    }
    return render(request,"data.html",context)
  
  
def search(request):
    if request.method=="POST":
        searchd = request.POST.get("search")
        print(searchd)
        
        vanue= student_info.objects.filter(Roll_no=searchd)
        print(vanue)
        
        
        # context={
        #     'searchd': searchd,
        #     'vanue':vanue
        # }
        return render(request,"search.html",{'searchd':searchd,'vanue':vanue})
    
    else:
     return render(request,"search.html")
 
 
def attendance(request):
    if request.method=="POST":
        
        attendance= request.POST.get("attendance")
        att= attendane.objects.all()
        
        record = attendane(attendane=attendance)
        
        record.save()
        
        context={
            'att':att
        }
        return render(request,"attendance.html",{'att':att})
    
    else:
        return render(request,"attendance.html")
    
    
    
