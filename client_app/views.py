from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee
# Create your views here.

def index(request):
    return HttpResponse(f"<h1>{request.tenant} index</h1>")


def create_employee(request, name):
    employee= Employee(name=name)
    employee.save()
    return HttpResponse(f"<h1>{request.tenant} employee created</h1>")