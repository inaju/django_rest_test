from django.shortcuts import render, HttpResponse
import requests
import socket    

# Create your views here.

def home(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    
    return render(request, 'core/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_data']
    })
    

def weather(request):

    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)  
    print(IPAddr)
    url = "http: // ip-api.com/json/24.48.0.1"
    print(url)

    response = requests.get(url)
    data = response.json()
    print(response.text) 
    return HttpResponse(response.text)

