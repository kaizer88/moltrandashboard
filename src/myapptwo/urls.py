from django.urls import path
from .views import list_app_two


urlpatterns = [

    path('list', list_app_two, name='list_app_two'),

]
