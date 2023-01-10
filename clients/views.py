from django.shortcuts import render
from django.http import HttpResponse

from clients.models import Clients
from clients.forms import ClientForm


def add_client(request):
    if request.method == 'GET':
        context = {
            'form': ClientForm()
        }

        return render(request, 'clients/add_client.html', context=context)

    elif request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            Clients.objects.create(
                name=form.cleaned_data['name'],
                last_name=form.cleaned_data['last_name'],
                age=form.cleaned_data['age'],
            )
            context = {
                'message': 'Cliente añadido Correctamente'
            }
            return render(request, 'clients/add_client.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ClientForm()
            }
            return render(request, 'clients/add_client.html', context=context)

def list_clients(request):
    if 'search' in request.GET:
        search = request.GET['search']
        clients = Clients.objects.filter(name__icontains=search)
    else:
        clients = Clients.objects.all()
    context = {
        'clients':clients,
    }
    return render(request, 'clients/list_clients.html', context=context)