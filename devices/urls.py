from django.urls import path
from . import views

# Registering the devices namespace to be used in the ticket_app urls.py
app_name = "devices"

# Defining url patterns for the devices app
urlpatterns = [
    # Root pattern, displaying all devices
    path("", views.all_devices, name="all_devices"),
    # URL for the create_device page
    path("new/", views.create_device, name="create_device"),
    # URL for the edit device page, passed a primary key to identify what device to edit
    path("<int:pk>/edit/", views.edit_device, name="edit_device"),
    # URL for the delete device page, passed a primary key to identify what device to delete
    path("<int:pk>/delete/", views.delete_device, name="delete_device"),
]
