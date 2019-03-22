from django.shortcuts import render
from django.http import HttpResponse
from sensors import container_temp, static_container
import json,os
print(os.getcwd())
STATIC_TEMP_FILE = 'sensors/temp.json'

def home(request):
    return render(request, 'home.html', {})

def temp(request):
    return render(request, 'temp.html', {})

def sockets(request):
    all_temps = container_temp.Container().temp_containter_list()
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
    return HttpResponse('')


