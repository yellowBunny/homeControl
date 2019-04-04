from django.shortcuts import render
from django.http import HttpResponse
from sensors import virtual_DHT11, container_temp, static_container
from request import req
import json, os, sys

print(os.getcwd())
STATIC_TEMP_FILE = 'sensors/temp.json'
TEST_STATIC_FILE = 'sensors/test_container.json'

def home(request):
    return render(request, 'home.html', {})

def temp(request):
    sensor = virtual_DHT11.DHT11()
    temp_salon = sensor.json_temp(10)
    temp_p1 = sensor.json_temp(20)
    temp_p2 = sensor.json_temp(21)
    temp_kitchen = sensor.json_temp(22)
    temp_bathroom = sensor.json_temp(23)
    return render(request, 'temp.html', {'temp_salon': temp_salon, 'temp_p1': temp_p1, 'temp_p2' : temp_p2,
                                         'temp_kitchen' : temp_kitchen, 'temp_bathroom': temp_bathroom},)

def sockets(request):
    return render(request, 'sockets.html', {})


def back(request):
    '''this method transform data to JSON format and send it to server'''
    print('jestes w views.back')
    temp_in_json = static_container.KeepTempInFile().read_from_json(STATIC_TEMP_FILE)
    if temp_in_json:
        json_data = json.JSONEncoder().encode(temp_in_json)
        return HttpResponse(json_data)
    print('DATA NOT DETECTED')
    container = container_temp.Container().temp_containter_list()
    json_data = json.JSONEncoder().encode(container)
    return HttpResponse(json_data)

def update_temp_data_in_json(request):
    '''this method update data in .json file'''
    print('IN UPDATE')
    container = container_temp.Container().temp_containter_list()
    static_container.KeepTempInFile().save_to_json(STATIC_TEMP_FILE, container)
    return HttpResponse('data was update!! {0}'.format(container))


def test_func(request):
    info = sys.version
    return HttpResponse(info)


def read_hours_and_minute(request):
    obj_req = req.ParsDataFromURL()
    data = obj_req.load_data_from_url('http://127.0.0.1:8000/sockets/')
    feetback = obj_req.parse_data(data, 'h3')
    return HttpResponse(feetback)



