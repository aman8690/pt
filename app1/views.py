from django.shortcuts import render
from django.http import HttpResponse
from .models import student

# Create your views here.

def login_registration(request):
  return  render(request,'login.html')

