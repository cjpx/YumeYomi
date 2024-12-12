from django.urls import path, include
from django.shortcuts import render
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.post, name="posts"),
    path("radicals/", views.radicals, name="radicals"),
    path("radical/<str:radical>", views.radical_detail, name="radical_detail"),

    path('radicals/search/', views.radical_selection, name='radical_selection'),
    path('fetch-characters/', views.fetch_characters, name='fetch_characters'),

    path('character/<str:name>/', views.character_detail, name='character_detail'),
    #path('character/<int:pk>/edit/', views.submit_edit, name='submit_edit'),

    path('generate_audio/', views.generate_audio, name='generate_audio'),
]