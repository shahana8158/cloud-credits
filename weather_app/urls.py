
from django.urls import path
from .import views
from weather_app import views
urlpatterns=[
    
    path('',views.home),
]