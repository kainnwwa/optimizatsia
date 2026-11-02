# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='start'),
    path('timer/', views.timer_page, name='timer'),
]