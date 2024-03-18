from django.urls import path
from . import views

# Registering the tickets namespace to be used in the ticket_app urls.py
app_name = "tickets"

urlpatterns = [
    # Root pattern displaying all tickets assigned to current user (admin) or raised by user (non admin)
    path("", views.ticket_list, name="ticket_list"),
    # URL for viewing all tickets
    path("all/", views.all_tickets, name="all_tickets"),
    # URL for created a new ticket
    path("new/", views.ticket_create, name="ticket_new"),
    # URL for viewing unassigned tickets 
    path("unassigned/", views.unassigned_tickets, name="unassigned_tickets"),
    # URL to assign a ticket
    path("assign_ticket/", views.assign_ticket, name="assign_ticket"),
    # URL to edit a ticket
    path("<int:pk>/edit/", views.ticket_update, name="ticket_edit"),
    # URL to delete a ticket
    path("<int:pk>/delete/", views.ticket_delete, name="ticket_delete"),
    # URL to mark ticket as resolved
    path("<int:pk>/resolve/", views.resolve_ticket, name="resolve_ticket"),
]
