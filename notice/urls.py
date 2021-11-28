from django.urls import path
from . import views
from .models import Notice


urlpatterns = [
    path('', views.notice, name='notice'),
    
    
    ]