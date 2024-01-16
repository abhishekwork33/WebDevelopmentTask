from django.contrib import admin
from django.urls import path, include, re_path
from . import views


app_name = 'backend'


urlpatterns = [
    path('', views.index, name ='indexpage')
    
]