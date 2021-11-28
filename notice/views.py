from django.shortcuts import render
from .models import Notice
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import authenticate

def notice(request):
    note = Notice.objects.filter().order_by('-date')
    return render(request,'notice/notice.html',{'notice':note})