from django.shortcuts import render
from django.http import HttpResponse
from sensors import dht11,ds18b20


def home(request):
    return render(request, 'home.html', {})

def temp(request):
    return render(request, 'temp.html', {})

def sockets(request):
    sensor = dht11.DHT11()
    temp = sensor.JSONtemp(16)
    return render(request, 'sockets.html', {'var': temp})

def temp1(request):
    
    return HttpResponse(temp)
