from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import *
from django.contrib import messages
from django.db.models import Q,aggregates,Sum
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
def welcome(request):
    return HttpResponse('<h1> welcome to the django server</h1>')



def information(request):
    data=STUDENT.objects.all()
    if request.GET.get('q'):
        search=request.GET.get('q')
        data=data.filter(
            Q(student_name__icontains=search)|
            Q(student_age__icontains=search)|
            Q(department__department__icontains=search)|
            Q(student_email__icontains=search)|
            Q(student_addre__icontains=search)|
            Q(student_id__student_id__icontains=search)
        )
    return render(request,'information.html',context={'data':data})
def register(request):
    if request.method=="POST":
        data=request.POST
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        username=data.get('username')
        password=data.get('password')
        name=User.objects.filter(username=username)
        if name.exists():
            messages.info(request,'user already exists')
            return redirect('/registration/')
        else:
            user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request,'register successfully')
        return redirect("/registration/")
    return render(request,'registration.html')
def enter(request):
    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,'Invalid password and user')
            return redirect('/login/')
        else:
            messages.info(request,'login successfully')
            login(request,user)
            return redirect('/information/')
    return render(request,'login.html')
def exit(request):
    return redirect('/login/')

def result(request,student_id):
    data=SUBJECTMARKS.objects.filter(student__student_id__student_id=student_id)
    total=0
    rank=STUDENT.objects.annotate(marks=Sum('studentmarks__mark')).order_by('-marks','-student_age')
    i=1
    rankk=-1
    for ranks in rank:
        if student_id==ranks.student_id.student_id:
            rankk=i
            break
        i=i+1
    for i in range(0,len(data)):
        total=total+data[i].mark
    name=STUDENT.objects.get(student_id__student_id=student_id).student_name
    return render(request,'marks.html',context={'data':data ,'total':total,'name':name,'rank':rankk})

