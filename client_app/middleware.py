from client_app.models import Employee

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        domain = request.get_host().split(':')[0]  # Extract domain
        request.tenant = Employee.objects.filter(domain=domain).first()
        return self.get_response(request)