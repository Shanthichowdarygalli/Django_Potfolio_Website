from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def home(request):
#     msg = '!!! Welcome, To Home page !!!'
#
#     return HttpResponse(msg)


#
# def contactus(request):
#     msg = '!!! Welcome, To contactus page !!!'
#
#     return HttpResponse(msg)


def contactus(request):
    #msg = '!!! Welcome, To contactus page !!!'

    return render(request,'contact us.html')#http://127.0.0.1:8000/contactus/


def home(request):
    #msg = '!!! Welcome, To Home page !!!'

    return render(request,'Home page.html') #http://127.0.01:8000/home/
