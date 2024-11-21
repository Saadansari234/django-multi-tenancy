from django.contrib import admin

from .admin_site import client_admin_site
from .models import Employee  # Replace with actual models

# admin.register(Employee, site=client_admin_site)
class ClientAppModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if hasattr(request, 'tenant'):
            return qs.filter(tenant=request.tenant)  # Filter by tenant
        return qs

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If creating a new object
            obj.tenant = request.tenant  # Assign current tenant
        super().save_model(request, obj, form, change)
        
        
client_admin_site.register(Employee , ClientAppModelAdmin)       