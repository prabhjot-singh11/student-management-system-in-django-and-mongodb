"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='home'),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("signout",views.signout,name="signout"),
    path("add",views.add,name="add"),
    path("add_student",views.add_student,name="add_student"),
    path("student_data",views.student_data,name="student_data"),
    # path("update",views.update,name="update"),
    # path("data/<Roll_no>",views.data,name="data")
    path("ex",views.ex,name="ex"),
    path("search",views.search,name="search"),
    path("attendance",views.attendance,name="attendance")
]
