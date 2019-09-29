from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.

def home(request):
    response = requests.post('https://trackapi.nutritionix.com/v2/natural/nutrients', headers={"x-app-id":"4e13e5aa","x-app-key":"2371b979c007fdf88758574145c58171"},data={"query":"eggs for breakfast"})
    return JsonResponse(response.json())
