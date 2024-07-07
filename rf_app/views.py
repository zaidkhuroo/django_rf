from django.shortcuts import render
from django.http import JsonResponse

# DRF library import
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import APIView
from rest_framework.response import Response

from . import serializers
from .models import Post

# Create your views here.
class TestView(APIView):
    permission_classes=(IsAuthenticated,)
    
    def get(self,request):
        queryset= Post.objects.all()
        serializer=serializers.TestSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = serializers.TestSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)