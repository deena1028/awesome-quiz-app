from django.db import models

# Create your models here.

class  user_login(models.Model):
    username=models.TextField(max_length=200)
    userid=models.TextField(max_length=200)
    paswod=models.TextField(max_length=200)
class courses(models.Model):
    courseName=models.TextField(max_length=200)
    status=models.IntegerField(null=True)

class quizz(models.Model):
    quizname=models.TextField(max_length=200)
    courseId=models.ForeignKey(courses, null=True, on_delete=models.CASCADE)
    no_of_quest=models.IntegerField(null=True)
    quizDuration=models.TextField(max_length=20)
    status=models.IntegerField(null=True)
class questions(models.Model):
    question=models.TextField(max_length=500)
    courseId=models.ForeignKey(courses, null=True, on_delete=models.CASCADE)
    quizId=models.ForeignKey(quizz, null=True, on_delete=models.CASCADE)
    optA=models.TextField(max_length=200)
    optB=models.TextField(max_length=200)
    optC=models.TextField(max_length=200)
    optD=models.TextField(max_length=200)
    correctOpt=models.TextField(max_length=200)

    
    