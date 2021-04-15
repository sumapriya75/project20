from django.shortcuts import render
from django .http import HttpResponse
# Create your views here.
def index2(request):
    return HttpResponse("<h1>welcome to app2 of sample2</h1>")
def sample2(request):
    return render (request,"sample2.html")
