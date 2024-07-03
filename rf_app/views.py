from django.shortcuts import render
from django.http import JsonResponse

# DRF library import
from rest_framework.decorators import APIView
from rest_framework.response import Response

# Create your views here.
class TestView(APIView):
    def get(self,request,*args,**kwargs):
        data={
            'name':'Aabid',
            'age':22,
            'city':'Delhi'
        }
        return Response(data)