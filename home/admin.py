from django.contrib import admin
from .models import user_login,courses,quizz,questions
# Register your models here.

mymodel=[user_login,courses,quizz,questions]
admin.site.register(mymodel)