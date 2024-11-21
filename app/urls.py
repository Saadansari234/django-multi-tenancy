from django.contrib import admin
from django.urls import path, include
from app.views import index, create_client

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', index, name="index"),
  path("client/", include('client_app.urls')),
  path('create_client',create_client, name="create_client"),
]