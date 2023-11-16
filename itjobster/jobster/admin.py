from django.contrib import admin
from .models import *
# Register your models here.
class Useradmin(admin.ModelAdmin):
    list_display=("username","email","age","phone","location","aadhar","password")
admin.site.register(user,Useradmin)

class administratoradmin(admin.ModelAdmin):
    list_display=("adminname","adminpass")
admin.site.register(administrator,administratoradmin)


class companyadmin(admin.ModelAdmin):
    list_display=("gstin","companyname","location","contact","password")
admin.site.register(company,companyadmin)

# resumeapp/admin.py


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'email', 'phone','website','linkedin', 'degree','university','graduation_year','skills','spoken_languages','job_experience','personal_description')

admin.site.register(Resume, ResumeAdmin)


