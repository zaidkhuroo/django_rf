from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.TestView.as_view(), name='test')
    
]
