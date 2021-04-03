from django.urls import path
from .views import list_app_one


urlpatterns = [

    path('list', list_app_one, name='list_app_one'),

]
