from django.contrib import admin
from .models import student_info
from .models import attendane
from .models import name
# from .models import attendane
# Register your models here.
admin.site.register(student_info)
admin.site.register(attendane)
admin.site.register(name)