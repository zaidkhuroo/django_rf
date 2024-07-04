from django.shortcuts import render
from django.http import JsonResponse

# DRF library import
from rest_framework.decorators import APIView
from rest_framework.response import Response

from . import serializers
from . import models

# Create your views here.
class TestView(APIView):
    def get(self,request):
        data={
            'name':'Aabid',
            'age':22,
            'city':'Delhi'
        }
        return Response(data)
    
    def post(self,request):
        serializer = serializers.Testserializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)