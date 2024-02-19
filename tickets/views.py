from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket
from .forms import TicketForm


# Create your views here.
def index(request):
    return render(request,"index.html")

# Read
def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, "ticket_list.html", {'tickets': tickets})

# Create
def ticket_create(request):
    form = TicketForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/tickets/')
    return render(request, 'ticket_form.html', {'form': form})

# Update
def ticket_update(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    form = TicketForm(request.POST or None, instance=ticket)
    if form.is_valid():
        form.save()
        return redirect('/tickets/')
    return render(request, 'ticket_form.html', {'form': form})

# Delete
def ticket_delete(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('/tickets/')
    return render(request, 'ticket_confirm_delete.html', {'ticket': ticket})
