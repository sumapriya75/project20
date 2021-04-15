from django.shortcuts import render
from django.urls import path
from app3 import views
app_name="app3"
urlpatterns = [
    path("add/<num1>/<num2>/",views.add,name="add"),
]
    
