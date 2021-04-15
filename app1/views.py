from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index1 (request):
    return HttpResponse("<h1>welcome to app1 of index1</h1>")
def sample1(request):
    return render(request,"sample1.html")
