from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user_login,courses,questions

# Create your views here.
def index(request):
   return render(request,'index.html')
def login_user(request):
      if(request.method=="POST"):
             userid=request.POST.get('userid')
             paswod=request.POST.get('paswod')
             check_user =user_login.objects.filter(userid=userid,paswod=paswod)
             if check_user:
                   request.session['user'] = userid
                  
                   return redirect('/home')
def home(request):
      courseData=courses.objects.all()
      cData={'cData':courseData}
      return render(request,'dashboard.html',cData)
def quizz(request,id):
   dts=questions.objects.filter(courseId=id)
   print(dts)
   qData={'question':dts }
   return render(request,'quizz.html',qData)
   