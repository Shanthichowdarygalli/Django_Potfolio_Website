from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def hello(request):
#     msg = 'Welcome, To The Tasty cakes ***'
#     return HttpResponse(msg) #http://127.0.0.1:8000/cakes/hello/

def honey(request):
    #msg = 'Welcome, To The Tasty cakes ***'
    return render(request,'cakes/honey.html')








