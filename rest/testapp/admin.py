from django.contrib import admin
from .models import Emp
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ['id','eno','ename','esal','eadd']

admin.site.register(Emp,EmpAdmin)