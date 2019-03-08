from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('temp/', views.temp, name='temp'),
    path('sockets/', views.sockets, name='sockets'),

]
