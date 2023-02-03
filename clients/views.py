from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from clients.models import Clients
from clients.forms import ClientForm

@login_required
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

@login_required
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

def client(request):
    if 'search' in request.GET:
        search = request.GET['search']
        client = Clients.objects.filter(name__icontains=search)
    else:
        client = Clients.objects.all()
    context = {
        'client':client,
    }
    return render(request, 'clients/client.html', context=context)


@login_required
def update_client(request, pk):
    client = Clients.objects.get(id=pk)
    
    if request.method == 'GET':
        context = {
            'form': ClientForm(
                initial={
                    'name':client.name,
                    'last_name':client.last_name,
                    'age':client.age,
                    'address':client.address,
                    'phone_number':client.phone_number,
                    'email':client.email,
                }
            )
        }

        return render(request, 'clients/update_client.html', context=context)

    elif request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client.name = form.cleaned_data['name'],
            client.last_name = form.cleaned_data['last_name'],
            client.age = form.cleaned_data['age'],
            client.address = form.cleaned_data['address'],
            client.phone_number = form.cleaned_data['phone_number'],
            client.email = form.cleaned_data['email'],
            client.save()
            
            context = {
                'message': 'Proveedor actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': ClientForm()
            }
        return render(request, 'clients/update_client.html', context=context)

# class ProviderUpdateView(UpdateView)
# def provider_delete(request, pk):     //provider.delete()

class ClinetDeleteView(DeleteView):
    model = Clients
    template_name = 'clients/delete_client.html'
    success_url = '/clients/delete_client/'