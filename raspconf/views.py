from django.shortcuts import render
from django.http import HttpResponse
from sensors import container_temp
import json


def home(request):
    return render(request, 'home.html', {})

def temp(request):
    return render(request, 'temp.html', {})

def sockets(request):
    all_temps = container_temp.Container().temp_containter_list()
    return render(request, 'sockets.html', {})


def background_read_data_from_sensors(request):
    print('jestes w views.back')    
    container = container_temp.Container().temp_containter_list()
    print(container)
    test_data = [{'a': 1}, {'b':2}]
    json_data = json.JSONEncoder().encode(container)
    return HttpResponse(json_data)





