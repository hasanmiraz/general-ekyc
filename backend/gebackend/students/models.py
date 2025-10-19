from django.db import models

from .utils import student_upload_path

class Student(models.Model):
    student_number = models.CharField(max_length=32, unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    dob = models.DateField(null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(unique=True, null=True)
    addess = models.CharField(max_length=160, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=student_upload_path)
    
    class Meta:
        odering = ["-created"]
        
    def __str__(self) -> str:
        return f"{self.student_number} - {self.first_name} {self.last_name}"
    
    