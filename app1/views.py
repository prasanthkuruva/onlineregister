from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
# Create your views here.
from app1.models import Students, Login
from django.db import IntegrityError

def index(request):
    return render(request,"welcome.html")


def registration(request):
    if request.method=='POST':
        a=request.POST.get('t1')
        b=request.POST.get('t2')
        c=request.POST.get('t3')
        d=request.POST.get('t4')
        e=request.POST.get('t5')
        f=request.POST.get('t6')
        g=request.POST.get('t7')
        type='student'
        try:
            Students(name=a,age=b,contact_no=c,gender=d,email=e,username=f).save()
            Login(username=f,password=g,type=type).save()
            messages.success(request,"Successfully Registered")
            return redirect('registration')
        except IntegrityError:
            messages.success(request,'email or phone number alredy used')
            return redirect('registration')
    else:
     return render(request,'Registration.html',{"data":""})


def slogin(request):
    return render(request,'login.html')

def alog(request):
    return render(request,'alogin.html')


def forgot(request):
            return render(request,'forgot.html')



def ahome(request):
    if request.method=="POST":
        a=request.POST.get('t1')
        b=request.POST.get('t2')
        print(a,b)
        type='admin'
        try:
            Login.objects.get(username=a, password=b, type=type)
            return render(request, 'adminhome.html')
        except Login.DoesNotExist:
            messages.error(request,"Does not Exist")
            return redirect('alog')
    else:
        return render(request,'adminhome.html')


def aview(request):
    data=Students.objects.all()
    return render(request,'aview.html',{"data":data})


def shome(request):
    if request.method=='POST':
        a=request.POST.get('t1')
        b=request.POST.get('t2')
        type='student'
        try:
            Login.objects.get(username=a,password=b,type=type)
            return render(request,'srudenthome.html',{"name":a})
        except Login.DoesNotExist:
            messages.error(request,"User Doesn't Exist Register Here")
            return redirect('registration')
    if request.method=='GET':
        uname=request.GET.get('un')
        return render(request,'srudenthome.html',{'name':uname})



def sprofile(request):
    uname=request.GET.get('un')
    print(uname)
    stu=Students.objects.get(username=uname)
    print(stu)
    return render(request,'sprofile.html',{'name':uname,"data":stu})


def uprofile(request):
        uname=request.GET.get('un')
        stu=Students.objects.get(username=uname)
        return render(request,'uprofile.html',{'data':stu,"name":uname})
def updation(request):
        n=request.POST.get('t1')
        a = request.POST.get('t2')
        c = request.POST.get('t3')
        g = request.POST.get('t4')
        e = request.POST.get('t5')
        f = request.POST.get('t6')
        print(n,a,c,g,e,f)
        stu=Students.objects.filter(username=f).update(name=n,age=a,contact_no=c,gender=g,email=e)
        return render(request,'srudenthome.html',{"name":f,"data":"Profile Updated"})
def recover(request):
        u=request.POST.get('t1')
        m=request.POST.get('t2')
        try:
            Students.objects.get(username=u,email=m)
            obj=Login.objects.filter(username=u).get()
            subject = 'Your Recover Mail'

            send_mail(
                'This is Your Recover Mail',
                'hi'+' ' +str(u)+'\n'+'Your password is:'+str(obj.password),
                'kuruvaprashanth@gmail.com',
                [str(m),],
            )

            return render(request,'forgot.html',{'data':m})
        except Students.DoesNotExist:
            messages.error(request,"Invalid Credentials")
            return render(request,'forgot.html')


def adelete(request):
    data=Students.objects.all()
    return render(request,'adelete.html',{"data":data})
def dsuccess(request):
    uname = request.GET.get('un')
    Students.objects.filter(username=uname).delete()
    Login.objects.filter(username=uname).delete()
    print(uname)
    return render(request,'adminhome.html')