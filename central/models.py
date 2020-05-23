from django.db import models

# Create your models here.
class Student(models.Model):
    student_number = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=255, null=False)
    middle_initial = models.CharField(max_length=2, null=True)
    last_name = models.CharField(max_length=255, null=False)
    year_level = models.CharField(max_length=4, null=False)
    program = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)

    
