from django.contrib import admin
from .models import user_login,courses,courseQuizz,questions,userAnswer
# Register your models here.

mymodel=[user_login,courses,courseQuizz,questions,userAnswer]
admin.site.register(mymodel)