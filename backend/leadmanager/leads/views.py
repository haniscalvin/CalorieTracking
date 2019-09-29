from django.shortcuts import render
from django.http import JsonResponse
from .macro_code import macro_code_dict
import json
import requests
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)

# Create your views here.

def home(request):
    response = requests.post('https://trackapi.nutritionix.com/v2/natural/nutrients', headers={"x-app-id":"4e13e5aa","x-app-key":"2371b979c007fdf88758574145c58171"},data={"query":"eggs for breakfast"}).json()
    neutrient_array = response["foods"][0]["full_nutrients"]
    counter = 0
    for item in neutrient_array:
        try:
            neutrient_array[counter].update({ "macro":macro_code_dict[str(item['attr_id'])]})
        except Exception as ex:
            pass
        counter+=1
        # macro_code_dict[item['attr_id']]  

    nutrients_code = dict(nutrients=neutrient_array)
    
    # result = []
    # print()
    # for item in nutrients_code:
    #     result.push(macro_code.macro_code_dict[item["attr_id"].toString()])

    # return JsonResponse(json.dumps(nutrients_code),content_type='application/json')
    return HttpResponse(json.dumps(nutrients_code),content_type='application/json')