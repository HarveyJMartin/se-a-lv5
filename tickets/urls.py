from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    # path('',views.index, name="index"),
    path('', views.ticket_list, name='ticket_list'),
    path('all/', views.all_tickets, name='all_tickets'),
    path('new/', views.ticket_create, name='ticket_new'),
    path('unassigned/', views.unassigned_tickets, name='unassigned_tickets'),
    path('assign_ticket/', views.assign_ticket, name='assign_ticket'),
    path('<int:pk>/edit/', views.ticket_update, name='ticket_edit'),
    path('<int:pk>/delete/', views.ticket_delete, name='ticket_delete'),
]