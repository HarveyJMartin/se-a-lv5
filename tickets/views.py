from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket
from .forms import EditTicketForm, CreateTicketForm
from django.contrib.auth.decorators import login_required
from ticket_app.decorators import admin_required
from django.contrib import messages


# Create your views here.


# Read
@login_required
def all_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, "all_tickets.html", {"tickets": tickets})


# Read
@login_required
def ticket_list(request):
    is_admin = request.user.is_staff
    if is_admin is False:
        user_id = request.user.id
        tickets = Ticket.objects.filter(customer_id=user_id)
    elif is_admin is True:
        user_id = request.user.id
        tickets = Ticket.objects.filter(assigned_to_id=user_id)
    return render(request, "ticket_list.html", {"tickets": tickets})


@admin_required
def unassigned_tickets(request):
    tickets = Ticket.objects.filter(assigned_to_id=None)
    return render(request, "unassigned_tickets.html", {"tickets": tickets})


@admin_required
def assign_ticket(request):
    if request.method == "POST":
        ticket_id = request.POST.get("ticket_id")
        ticket = Ticket.objects.get(id=ticket_id)
        ticket.assigned_to = request.user
        ticket.save()
        messages.success(request, "Ticket successfully assigned!")
        return redirect(
            "tickets:ticket_list"
        )  # Redirect to an appropriate page after assignment
    else:
        return redirect("tickets:unassigned_tickets")  # Handle error or invalid access


# Create
@login_required
def ticket_create(request):
    form = CreateTicketForm(request.POST or None)
    if form.is_valid():
        ticket = form.save(commit=False)
        ticket.customer = request.user
        ticket.save()
        ticket.set_default_resolution()
        ticket.save()
        messages.success(request, "Ticket created successfully!")
        return redirect("/tickets/")
    return render(request, "create_ticket_form.html", {"form": form})


# Update
@login_required
def ticket_update(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    form = EditTicketForm(request.POST or None, instance=ticket)
    if form.is_valid():
        form.save()
        messages.success(request, "Ticket updated successfully!")
        return redirect("/tickets/")
    return render(
        request,
        "edit_ticket_form.html",
        {
            "form": form,
            "ticket": ticket,
        },
    )


# Delete
@admin_required
def ticket_delete(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        ticket.delete()
        return redirect("/tickets/")
    return render(request, "ticket_confirm_delete.html", {"ticket": ticket})


@login_required
def resolve_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    # Check if the user has permission to resolve the ticket
    if request.user == ticket.assigned_to or request.user.is_staff:
        ticket.resolved = True
        ticket.set_closed_date()
        ticket.save()
        messages.success(request, "Ticket marked as resolved successfully!")
        return redirect(
            "/tickets/"
        )  # Replace '/tickets/' with the actual path to the ticket list or detail view
