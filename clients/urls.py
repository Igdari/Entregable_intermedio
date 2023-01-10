from django.urls import path
from clients.views import add_client , list_clients

urlpatterns = [
    path('add-client/', add_client),
    path('list-clients/', list_clients),
]