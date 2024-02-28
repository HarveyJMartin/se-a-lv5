from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket
from .forms import FullTicketForm, CreateTicketForm
from django.contrib.auth.decorators import login_required
from ticket_app.decorators import admin_required


# Create your views here.


# Read
@login_required
def ticket_list(request):
    is_admin = request.user.is_staff
    if is_admin is False:
        user_id = request.user.id
        tickets = Ticket.objects.filter(customer_id=user_id)
    elif is_admin is True:
        user_id = request.user.id
        tickets = Ticket.objects.filter(assigned_to_id = user_id)
    return render(request, "ticket_list.html", {'tickets': tickets})


@admin_required
def unassigned_tickets(request):
    tickets = Ticket.objects.filter(assigned_to_id = None)
    return render(request, "unassigned_tickets.html", {'tickets': tickets})


# Create
@login_required
def ticket_create(request):
    form = CreateTicketForm(request.POST or None)
    if form.is_valid():
        ticket = form.save(commit=False)
        ticket.save()
        ticket.set_default_resolution()
        ticket.save()
        return redirect('/tickets/')
    return render(request, 'ticket_form.html', {'form': form})

# Update
@login_required
def ticket_update(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    form = FullTicketForm(request.POST or None, instance=ticket)
    if form.is_valid():
        form.save()
        return redirect('/tickets/')
    return render(request, 'ticket_form.html', {'form': form})

# Delete
@login_required
def ticket_delete(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('/tickets/')
    return render(request, 'ticket_confirm_delete.html', {'ticket': ticket})
