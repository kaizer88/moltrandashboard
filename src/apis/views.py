from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests
import json


# Create your views here.

@login_required()
def apidemo(request):
    context = {}
    response = requests.get('https://reqres.in/api/users')
    geodata = response.json()
    data = geodata['data']
    context['data'] = data
    # return render(request, 'core/home.html', {
    #     'ip': geodata['ip'],
    #     'country': geodata['country_name']
    # })

    return render(request, 'apis/apidemo.html', context)