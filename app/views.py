from pstats import Stats
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
import statistics
from unicodedata import name
from urllib import response
from django.contrib import messages
# from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from requests import Response
from django.contrib.auth.hashers import make_password

from app.models import Customer, Appointment, report

# Create your views here.
def home_view(request):
    return render(request,'home.html')

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    return render(request,'contact.html')

def signin_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"success")
            return redirect("/")
        else:
           messages.error(request,"Invalid")  
        #    ALERT_DESCRIPTION_ACCESS_DENIED("")
    return render(request,'Login.html')

def signout(request):
    logout(request)
    return redirect('/')    

def customer_view(request):
    if request.method=="POST":
        cus_username = request.POST.get('uname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('add')
        contact=Customer.objects.create(cus_username=cus_username,email=email,phone=phone,address=address)
        contact.save()
        if contact:
            messages.success(request,"success")
        else:
            messages.success(request,"Not success")

    return render(request,'contact.html')

def contact(request):
    data=Customer.objects.all()
    context={'show':data}
    return render(request,'viewcontact.html',context)

def appointment(request):
    data=Appointment.objects.all()
    context={'show':data}
    return render(request,'viewappointment.html',context)

def appointment_view(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            appointment_name=request.POST.get('name')
            appointment_service=request.POST.get('service')
            appointment_date=request.POST.get('date')
            appointment_time=request.POST.get('time')
            # appointment_message=request.POST.get('message')
            app=Appointment.objects.create(appointment_name=appointment_name,appointment_service=appointment_service,appointment_date=appointment_date,appointment_time=appointment_time)
            app.save()
            if app:
                messages.success(request,"Appointment success")
                return redirect("/")


            else:
                messages.success(request,"Appointment Not successful")

        return render(request,'appointment.html')
    else:
        return redirect("/Login/")


def signup_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.objects.create_user(username=username,email=email,password=password,first_name=fname, last_name=lname)

        user.save()

        if user:
            return redirect("/Login/")

    return render(request,'signup.html')



def doctors_view(request):
    return render(request, 'doctors.html')

def services_view(request):
    return render(request,'services.html')

def dashboard_view(request):
     return render(request,'dashboard.html')


def view_report(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            patient_name=request.POST.get('name')
            address=request.POST.get('address')
            contact=request.POST.get('contact')
            doctor=request.POST.get('doctor')
            detail=request.POST.get('detail')
            treatment=request.POST.get('treatment')
            recommendation=request.POST.get('recommendation')

            rep=report.objects.create(patient_name=patient_name,address=address,contact=contact,doctor=doctor,detail=detail,treatment=treatment,recommendation=recommendation)
            rep.save()
            if rep:
                messages.success(request,"Report success")
                return redirect("/")


            else:
                messages.success(request,"Report Not successful")

        return render(request,'report.html')
    else:
        return redirect("/dashboard/") 

def Report(request):
    data=report.objects.all()
    context={'show':data}
    return render(request,'viewreport.html',context)
  

    
    



