from django.contrib.admin import AdminSite


class ClientAdminSite(AdminSite):
    site_header = "Client App Administration"
    site_title = "Client App Admin Portal"
    index_title = "Welcome to Client App Admin"

client_admin_site = ClientAdminSite(name='client_admin')