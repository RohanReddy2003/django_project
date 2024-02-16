from django.contrib import admin
from .models import Department,Elective,ElectivesInfo,StudentInfo,RegistrationTime
# Register your models here.
admin.site.register(Department)
admin.site.register(Elective)
admin.site.register(ElectivesInfo)
admin.site.register(StudentInfo)
admin.site.register(RegistrationTime)