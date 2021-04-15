from django.shortcuts import render
from django.urls import path
from app1 import views
app_name="app1"
urlpatterns = [
    path('',views.index1,name="index1"),
    path('sample1/',views.sample1,name="sample1"),
   
]
