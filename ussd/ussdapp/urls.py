from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('ussd/',views.index,name="index"),
]