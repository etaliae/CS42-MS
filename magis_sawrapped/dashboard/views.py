from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return HttpResponse('Hello, World!')

# Create your views here.
