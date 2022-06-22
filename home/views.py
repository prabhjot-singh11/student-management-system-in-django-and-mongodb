from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate, login
from .models import student_info
from .forms import studentr

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
        print("dfhaifh")








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
    
 
    print("sssss")
    fname = request.POST.get("firstname")
    lname = request.POST.get("lsname")
    date = request.POST.get("dat")
    gender = request.POST.get("gender") 
    contect = request.POST.get("contect")
    email = request.POST.get("email")
    course = request.POST.get("course")
    address = request.POST.get("address")
    
    
    
    
    students= student_info(first_name = fname,last_name = lname,dob=date,gender =gender,contect =contect,  email = email,course =course,address=address )
    students.save()
    

  return render(request,"add.html")



def student_data(request):
    allstudents = student_info.objects.all()
    
    
    
    
    
    return render(request,"info.html",{'studentinfo' :allstudents})

def data(request):
    allstudents = student_info.objects.all()
    
    
    return render(request,"data.html",{'studentinfo' :allstudents})
def update(request,Roll_no):
    
#   allstudents= (student_info,id = id)
      allstudents= student_info.objects.get(Roll_no=Roll_no)
#   if request.method =="POST":
      allstudents.delete()
      return render(request,"show.html",{"del":allstudents})
    
    