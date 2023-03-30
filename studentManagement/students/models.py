from django.db import models

# Create your models here.

class Student(models.Model):
    student_num = models.PositiveIntegerField()
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=100)
    course = models.CharField(max_length=50)

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'

class Teacher(models.Model):
    teacher_num = models.PositiveIntegerField()
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return f'Teacher: {self.first_name} {self.last_name}'

class Parent(models.Model):
    parent_num = models.PositiveIntegerField()
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f'Parent: {self.first_name} {self.last_name}'
