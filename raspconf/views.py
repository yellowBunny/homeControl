from django.shortcuts import render
from django.http import HttpResponse
from sensors import container_temp
import json


def home(request):
    return render(request, 'home.html', {})

def temp(request):
##    sensor = virtual_DHT11.DHT11()
##    temp_salon = sensor.json_temp(10)
##    temp_p1 = sensor.json_temp(20)
##    temp_p2 = sensor.json_temp(21)
##    temp_kitchen = sensor.json_temp(22)
##    temp_bathroom = sensor.json_temp(23)
    return render(request, 'temp.html', {})

def sockets(request):
    all_temps = container_temp.Container().temp_containter_list()
    return render(request, 'sockets.html', {})


def back(request):
    print('jestes w views.back')
    # container = container_temp.Container().temp_containter_list()
    container = container_temp.Container().temp_containter_list()
    print(container)
    test_data = [{'a': 1}, {'b':2}]
    json_data = json.JSONEncoder().encode(container)
    return HttpResponse(json_data)





