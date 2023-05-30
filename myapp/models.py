from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Course(models.Model):
    courseid = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=20)

class Student(models.Model):
    cms = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=30)
    email = models.TextField(max_length=25)
    father_name = models.TextField(max_length=30)
    dept = models.TextField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)




