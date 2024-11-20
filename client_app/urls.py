# from django.contrib import admin
from django.urls import path

from .views import index, create_employee

urlpatterns = [
    path('', index, name="client_index"),
    path('create_employee/<name>',create_employee, name="create_employee")
]