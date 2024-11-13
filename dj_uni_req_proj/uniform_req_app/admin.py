from django.contrib import admin

from .models import Employee, Uniform, EmployeeUniform, UniformRequest, UniformRequestItem

# Register your models here.

admin.site.register(Employee)
admin.site.register(Uniform)
admin.site.register(EmployeeUniform)
admin.site.register(UniformRequest)
admin.site.register(UniformRequestItem)