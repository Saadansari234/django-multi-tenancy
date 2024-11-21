from django.shortcuts import render,redirect,HttpResponse
from .models import Client, Domain
# Create your views here.


def index(request):
    client= Client.objects.all()
    domain=Domain.objects.all()
    # print(context.client)
    return render(request, "index.html", {"clients":client, "domains":domain})


def create_client(request):
    if request.method == "POST":
        client_name = request.POST.get("client")
        domain_name = request.POST.get("domain")
        
        tenant = Client(name=client_name, schema_name=client_name.lower())
        tenant.save()

        domain = Domain(domain=domain_name, tenant=tenant, is_primary=True)
        domain.save()

        return redirect("index")
    else:
        return HttpResponse("Invalid request method", status=400)