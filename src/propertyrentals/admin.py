from django.contrib import admin
from .models import Country, Province, Property, Town, Address, Tenant, Agent, Profile


# Register your models here.
myModels  = [Country, Province, Property, Town, Address, Tenant, Agent, Profile]
admin.site.register(myModels)