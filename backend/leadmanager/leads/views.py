from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'test.html', {
    })