from django.urls import path
from .views import towns, properties, tenants, agents
from .views import edit_town, uploadlist, upload

urlpatterns = [

    path('towns', towns, name='towns'),
    path('add_town', edit_town, name='add_town'),
    path('edit_town/<pk>', edit_town, name='edit_town'),
    path('properties', properties, name='properties'),
    path('tenants', tenants, name='tenants'),
    path('agents', agents, name='agents'),
    path('uploadlist', uploadlist, name='uploadlist'),
    path('upload', upload, name='upload'),

]
