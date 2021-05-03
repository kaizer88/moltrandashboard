from django.urls import path
from .views import clients, edit_client, edit_client_plan

urlpatterns = [

    path('clients', clients, name='clients'),

    path('add_client', edit_client, name='add_client'),
    path('add_client_plan', edit_client_plan, name='add_client_plan'),

    path('edit_client/<id>', edit_client, name='edit_client'),
    # path('add_client_plan', edit_client_plan, name='add_client_plan'),
    path('update_subscription/<id>', edit_client_plan, name='update_subscription'),


]
