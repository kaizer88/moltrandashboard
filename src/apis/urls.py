
from django.urls import path
from .views import apidemo


urlpatterns = [

    path('', apidemo, name='apidemo'),

]

