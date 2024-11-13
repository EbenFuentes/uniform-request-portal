from django.db import models
from django.db.models import UniqueConstraint

# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(max_length=10)
    dob = models.DateField("dateOfBirth")
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, DOB: {self.dob}"

class Uniform(models.Model):
    TYPE_CHOICES = [
        ('White Polo', 'White Polo'),
        ('Black Pants', 'Black Pants')
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES, unique=True)

    def __str__(self):
        return f"{self.type}"
    
class EmployeeUniform(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    uniform = models.ForeignKey(Uniform, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['employee', 'uniform'], name='unique_employee_uniform')
        ]

class UniformRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Fulfilled', 'Fulfilled')
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    reason = models.TextField(blank=True, null=True)  # Optional reason for the request

    def __str__(self):
        return f"Request by {self.employee.employee_id} - Status: {self.status} - Date: {self.request_date}"

class UniformRequestItem(models.Model):
    request = models.ForeignKey(UniformRequest, on_delete=models.CASCADE, related_name="items")
    uniform = models.ForeignKey(Uniform, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.uniform.type} - Qty: {self.quantity} for Request ID: {self.request.id}"