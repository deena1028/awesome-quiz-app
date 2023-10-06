from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
   
    path('',views.index),
    path('login_user',views.login_user),
    path('home',views.home),
    path('quizz/<id>',views.quizz),
    path('update_user_answer',views.update_user_answer),
    path('result/<id>',views.result),
    path('signup',views.signup),
    path('signup_user',views.signup_user),
    path('logout',views.logout)
    
]