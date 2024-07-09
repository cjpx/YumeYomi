from django.urls import path, include
from django.shortcuts import render
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.post, name="posts"),
    path("radicals/", views.radicals, name="radicals"),
    path("radical/<str:radical>", views.radical_detail, name="radical_detail"),

    path('generate_audio/', views.generate_audio, name='generate_audio'),
]