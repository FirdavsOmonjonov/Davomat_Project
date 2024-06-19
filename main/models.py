from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Staff(models.Model):
    """Xodim"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    staff_position = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

def default_date():
    return timezone.now().date()

class Attendance(models.Model):
    """Davomat"""
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date_came = models.DateField(null=True, blank=True)  
    date_gone = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.staff.first_name + ' ' + self.staff.last_name

