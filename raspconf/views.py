from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})

def temp(request):
    return render(request, 'temp.html', {})

def sockets(request):
    return render(request, 'sockets.html', {})
