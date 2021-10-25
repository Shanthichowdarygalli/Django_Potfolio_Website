from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def hi(request):
#     msg = '!!! Welcome, To Django !!!'
#
#     return HttpResponse(msg)


def offer(request):
    #msg = '!!! Welcome, To Django !!!'

    return render(request,'fruits/apple.html')










