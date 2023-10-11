from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('generate', views.generate, name='generate'),
    path('draw', views.draw, name='draw'),
]
