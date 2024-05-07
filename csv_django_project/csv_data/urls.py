from django.urls import path
from .views import read_csv, register

urlpatterns = [
    path('csv/', read_csv, name='read_csv'),
    path('register/', register, name='register'),

]
