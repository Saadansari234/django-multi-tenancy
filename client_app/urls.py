from django.contrib import admin
from django.urls import path
from .admin import client_admin_site
# from .views import index, create_employee
from client_app import views

urlpatterns = [
    path('', views.index, name="client_index"),
    path('client-admin/', client_admin_site.urls), 
    path('create_employee/',views.create_employee.as_view(), name="create_employee"),
]