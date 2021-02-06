from django.contrib import admin
from myapp.models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address']

# admin.site.register(Student, StudentAdmin)
