from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
# Create your views here.
def carry_data(request,data):
    return HttpResponse(f'<h1> the received data is {data}</h1>')
def add(request,num1,num2):
    try:
        num1=int(num1)
    except:
        num1=float(num1)
    try:
        num2=int(num2)
    except:
        num2=float(num2)
    return HttpResponse(num1+num2)