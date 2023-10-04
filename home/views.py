from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import user_login,courses,questions,courseQuizz,userAnswer
import json
from json import dumps
import ast
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
      
       
            dts=questions.objects.filter(courseId=id).order_by("?")
            js=[]
            for i in dts:
                  js.append({'id':i.id,'question':i.question,'A':i.optA,'B':i.optB,'C':i.optC,'D':i.optD,'ans':i.correctOpt})
                  qduration=i.quizId.quizDuration
            quizz={'js':js}
            dataJSON = dumps(quizz) 
            
            
            qData={'question':dataJSON,'questids':'1' ,'count':int(0),'time':qduration}
            return render(request,'quizz.html',qData)
def update_user_answer(request):
      is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
      if is_ajax:
            if request.method == 'POST':
                  data = json.load(request)
                  userans=data.get("userAnsData")
                  qid=userans[0]['qid']
                  #question object
                  quest=questions.objects.get(id=qid) 
                  #course object
                  c=courses.objects.get(id=quest.courseId.id) 
                  #quizz object
                  quzid=courseQuizz.objects.get(id=quest.quizId.id) 
                  #userobject
                  users=user_login.objects.get(userid=request.session['user'])
                  query=userAnswer(courseId=c,quizId=quzid,user=users,userAns=userans)
                  query.save()
                  ids=userAnswer.objects.last().id
                  return JsonResponse({'id':ids})
                  
                  

def result(request,id):
      users=user_login.objects.get(userid=request.session['user'])
      userAns=userAnswer.objects.get(id=id)
      data=userAns.userAns
      cans=0
      dict_obj = ast.literal_eval(data)
      for i in dict_obj:
            a=i['userAns'].lower()
            b=i['ans'].lower()
            if a==b :
                  cans+=1
      quzid=courseQuizz.objects.get(id=userAns.quizId.id)    
      data={'usermark':cans,'total':quzid.no_of_quest}         
      return render(request,'end.html',data)
def signup(request):
      return render(request,'signup.html')
        
def signup_user(request):
      if(request.method=="POST"):
             uname=request.POST.get('username')
             userid=request.POST.get('userid')
             paswod=request.POST.get('paswod')
             query=user_login(username=uname,userid=userid,paswod=paswod)
             query.save()
             request.session['user'] = userid
             return redirect('/home')      
      
   