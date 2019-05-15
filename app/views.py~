from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import signin

def home(request):
    my_dict = {'insert_me' : "Hello World"}
    return render (request, 'first_app/signin.html', context=my_dict)

def something(request):
    my_dict = {'insert_me' : "Hello World"}
    return render (request, 'first_app/signup.html', context=my_dict)

def everything(request):
    my_dict = {'insert_me' : "Hello World"}
    return render (request, 'first_app/forgot.html', context=my_dict)

def anything(request):
    my_dict = {'insert_me' : "Hello World"}
    return render (request, 'first_app/details.html', context=my_dict)

def nothing(request):
    my_dict = {'insert_me' : "Hello World"}
    return render (request, 'first_app/page3.html', context=my_dict)


def parking(request) :
    email = request.POST["email"]
    password = request.POST["password"]

    sign_in = signin(email = email, password = password)
    sign_in.save()
    return render(request, "first_app/signin.html")

def parking1(request) :
    username = request.POST["username"]
    email = request.POST["email"]   
    password = request.POST["password"]
    confirm_password = request.POST["confirm_password"]
    date_birth = request.POST["date_birth"]

    sign_up = signup(username = username,email = email, password = password, confirm_password = confirm_password, date_birth = date_birth)
    sign_up.save()
    return render(request, "first_app/signup.html")


def parking2(request) :
    username = request.POST["username"]
    email = request.POST["email"] 
    date_birth = request.POST["date_birth"]  
    new_password = request.POST["new_password"]
    confirm_password = request.POST["confirm_password"]
   

    forgot = forgot(username = username,email = email, date_birth = date_birth, new_password = new_password, confirm_password = confirm_password)
    forgot.save()
    return render(request, "first_app/forgot.html")


    
def parking3(request) :
    vehicle_type = request.POST["vehicle_type"]
    vehicle_num = request.POST["vehicle_num"]   
    slot_time = request.POST[" slot_time"]
    slot_date = request.POST["slot_date"]

    details = details(vehicle_type = vehicle_type, vehicle_num =  vehicle_num, slot_time = slot_time, slot_date = slot_date)
    details.save()
    return render(request, "first_app/details.html")
