from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse(f"<h1>{request.tenant}</h1>")
