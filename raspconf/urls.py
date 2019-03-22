from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('temp/', views.temp, name='temp'),
    path('sockets/', views.sockets, name='sockets'),
    path('back/', views.back, name='background'),
    path('update/', views.update_temp_data_in_json, name='update'),
]
