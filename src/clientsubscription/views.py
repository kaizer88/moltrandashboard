from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Client
from .forms import *


# Create your views here.


@login_required()
def clients(request):
    context = {}
    clients = Client.objects.all()
    context['queryset'] = clients
    context['page'] = 'Client List'
    return render(request, 'clientsubscription/clients.html', context)

@login_required()
def edit_client(request, id= None):
    context = {}
    if id:
        client = Client.objects.get(pk=id)
        client_form = ClientForm(request.POST or None, instance=client)
    else:
        client_form = ClientForm(request.POST or None, auto_id=False)

    if client_form.is_valid():
        if not id:
            client = client_form.save(commit=False)
            client.created_by_id = request.user.id
            client.save()
            messages.success(request, 'client created')


        else:
            client = client_form.save(commit=False)
            client.save()
            messages.success(request, 'client  updated')

        return redirect('clients')

    context['form'] = client_form
    context['town'] = id
    # context['parent'] = 'Admin'
    context['add_page'] = 'Add Client'
    context['edit_page'] = 'Edit Client'
    return render(request, 'clientsubscription/edit_client.html', context)

@login_required()
def edit_client_plan(request, id= None):
    context = {}
    if id:
        client = Client.objects.get(pk=id)
        client_form = ClientPlanForm(request.POST or None, instance=client)
    else:
        client_form = ClientPlanForm(request.POST or None, auto_id=False)

    if client_form.is_valid():
        if not id:
            client = client_form.save(commit=False)
            client.created_by_id = request.user.id
            client.save()
            messages.success(request, 'client created')

        else:
            client = client_form.save(commit=False)
            client.save()
            messages.success(request, 'client  updated')

        return redirect('clients')

    context['form'] = client_form
    context['town'] = id
    # context['parent'] = 'Admin'
    context['add_page'] = 'Add Client'
    context['edit_page'] = 'Edit Client'
    return render(request, 'clientsubscription/edit_client_plan.html', context)