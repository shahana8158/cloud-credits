from django.urls import path
from .views import indexpage

urlpatterns = [
    path('', indexpage, name='convert_currency'),
]
