from django.db import models

# Create your models here.

class Attendance(models.Model):
    student_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    attendance_date = models.DateField()