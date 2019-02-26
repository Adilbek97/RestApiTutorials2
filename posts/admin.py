from django.contrib import admin
from .models import Teacher, Student, Subject, Questions, Result

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Questions)
admin.site.register(Result)