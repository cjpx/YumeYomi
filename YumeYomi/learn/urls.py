from django.urls import path, include
from django.shortcuts import render
from .import views

urlpatterns = [
    path("", views.home, name="home"),

    path('generate_audio/', views.generate_audio, name='generate_audio'),
]