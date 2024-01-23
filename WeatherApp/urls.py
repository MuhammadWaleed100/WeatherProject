from django.contrib import admin
from django.urls import path, include
from WeatherApp import views
urlpatterns = [
    path('', views.index, name='index'),
    path('full_details/', views.full_details, name='full_details')
]
    