from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=100)


class Teacher(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    login = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=30)


class Student(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    login = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=30)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, related_name='subjects', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='subjects', on_delete=models.CASCADE)


class Questions(models.Model):
    subject = models.ForeignKey(Subject, related_name='questions', on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    option_A = models.CharField(max_length=300)
    option_B = models.CharField(max_length=300)
    option_C = models.CharField(max_length=300)
    option_D = models.CharField(max_length=300)
    correct_option = models.CharField(max_length=3)


class Result(models.Model):
    student = models.ForeignKey(Student, related_name='results', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='results', on_delete=models.CASCADE)
    result = models.FloatField()
