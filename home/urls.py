from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
   
    path('',views.index),
    path('login_user',views.login_user),
    path('home',views.home),
    path('quizz/<id>',views.quizz),
]