from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import *
# from appuser.models import *
from django.contrib import messages
import sqlite3
from .models import Town, Property, Tenant, Agent, Profile
from .forms import TownForm, UploadForm
import time

import csv
from .forms import *

@login_required()
def towns(request):
    context = {}
    towns = Town.objects.all()
    context['queryset'] = towns
    context['page'] = 'Town List'
    return render(request, 'propertyrentals/towns.html', context)

@login_required()
def edit_town(request, id= None):
    context = {}
    if id:
        town = Town.objects.get(pk=id)
        town_form = TownForm(request.POST or None, instance=town)
    else:
        town_form = TownForm(request.POST or None, auto_id=False)

    if town_form.is_valid():
        if not id:
            town = town_form.save(commit=False)
            town.created_by_id = request.user.id
            town.save()
            messages.success(request, 'town created')

        else:
            town = town_form.save(commit=False)
            town.save()
            messages.success(request, 'town  updated')

        return redirect('towns')

    context['form'] = town_form
    context['town'] = id
    # context['parent'] = 'Admin'
    context['add_page'] = 'Add Towm'
    context['edit_page'] = 'Edit Town'
    return render(request, 'propertyrentals/edit_town.html', context)


@login_required()
def properties(request):
    context = {}
    properties = Property.objects.all()
    context['queryset'] = properties
    context['page'] = 'Property List'
    return render(request, 'propertyrentals/properties.html', context)

@login_required()
def edit_property(request, id= None):
    context = {}
    if id:
        town = Town.objects.get(pk=id)
        town_form = TownForm(request.POST or None, instance=town)
    else:
        town_form = TownForm(request.POST or None)

    if town_form.is_valid():
        if not id:
            town = town_form.save(commit=False)
            town.created_by_id = request.user.id
            town.save()
            messages.success(request, 'town created')

        else:
            town = town_form.save(commit=False)
            town.save()
            messages.success(request, 'town  updated')

        return redirect('district_list')

    context['form'] = town_form
    context['district'] = id
    context['parent'] = 'Admin'
    context['add_page'] = 'Add A District'
    context['edit_page'] = 'Edit District'
    return render(request, 'propertyrentals/edit_town.html', context)

@login_required()
def tenants(request):
    context = {}
    tenants = Tenant.objects.all()
    context['queryset'] = tenants
    context['page'] = 'Tenant List'
    return render(request, 'propertyrentals/tenants.html', context)

@login_required()
def agents(request):
    context = {}
    agents = Agent.objects.all()
    context['queryset'] = agents
    context['page'] = 'Agent List'
    return render(request, 'propertyrentals/agents.html', context)


@login_required()
def uploadlist(request):
    context = {}
    profiles = Profile.objects.all().order_by('-id')[:10]
    context['queryset'] = profiles
    context['page'] = 'Upload List'
    return render(request, 'propertyrentals/uploadlist.html', context)


@login_required()
def upload(request, id= None):
    context = {}

    upload_form = UploadForm(request.POST or None, request.FILES or None)
            # paramFile = request.FILES[''].read()
    # a = upload_form.files['upload']
    if upload_form.is_valid():
        item = []
        a = ()
        file = request.FILES['upload'].read().decode('utf-8').splitlines()
        raw = request.FILES['upload'].read()
        # decoded_file = file.read().decode('utf-8').splitlines()
        data = csv.DictReader(file)
        for row in data:
            # print(row['Name'])
            item.append((
                row['Id'],
                row['Name'],
                row['Surname'],
                row['Initials'],
                row['Age'],
                row['DateOfBirth']
            ))
        a =  item
        conn = sqlite3.connect("db.sqlite3")

        start = time.process_time()
        cur = conn.cursor()
        cur.executemany('insert into propertyrentals_profile values (?,?,?,?,?,?)', item)
        conn.commit()
        print(time.process_time() - start)
        print('Finisheeeeddd')
        return redirect('uploadlist')

    context['form'] = upload_form
    context['district'] = id
    context['parent'] = 'Admin'
    context['add_page'] = 'Upload'
    context['edit_page'] = 'Upload'
    return render(request, 'propertyrentals/upload.html', context)