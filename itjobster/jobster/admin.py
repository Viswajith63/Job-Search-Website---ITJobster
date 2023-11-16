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
    list_display=("cid","gstin","companyname","location","contact","password")
admin.site.register(company,companyadmin)

# resumeapp/admin.py


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'email', 'phone','website','linkedin', 'degree','university','graduation_year','skills','spoken_languages','job_experience','personal_description')

admin.site.register(Resume, ResumeAdmin)


class postjobAdmin(admin.ModelAdmin):
    list_display=('jid','jtitle','jlocation','jtype','jskills','jexperience','jvacancies')
admin.site.register(postjob,postjobAdmin)


class cprofileAdmin(admin.ModelAdmin):
    list_display = ('cname','cwebsite','clocations','jpostername','jposterdesignation','jposteremail','jposterphone','description')
admin.site.register(cprofile,cprofileAdmin)