from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.shortcuts import render

# Create your views here.


class HelloApiView(APIView):
    """API"""

    def get(self, request, format=None):
        myapi = request("")
        context = {}
        obj = [
            'test',
            'test2',
            'test3'
        ]
        context['obj'] = obj
        return Response(context=context)

