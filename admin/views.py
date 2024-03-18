from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AdminRequest
from .forms import AdminRequestForm
from ticket_app.decorators import admin_required
from django.contrib import messages


@login_required
def submit_admin_request(request):
    if request.method == "POST":
        form = AdminRequestForm(request.POST)
        if form.is_valid():
            admin_request = form.save(commit=False)
            admin_request.user = (
                request.user
            )  # Set the user to the currently logged-in user
            admin_request.save()
            messages.success(request, "Admin privilege request successfully raised!")
            return redirect("tickets:ticket_list")
    else:
        form = AdminRequestForm()
    return render(request, "admin_request_form.html", {"form": form})


@admin_required
def manage_admin_requests(request):
    if request.user.is_staff:
        admin_requests = AdminRequest.objects.filter(status="pending")
        return render(
            request, "manage_admin_requests.html", {"admin_requests": admin_requests}
        )
    else:
        return redirect("tickets:ticket_list")


@admin_required
def approve_request(request, request_id):
    admin_request = AdminRequest.objects.get(id=request_id)
    admin_request.status = "approved"
    admin_request.save()
    user = admin_request.user
    user.is_staff = True
    user.save()
    messages.success(request, "Request approved!")
    return redirect("admin:manage_admin_requests")


@admin_required
def reject_request(request, request_id):
    admin_request = AdminRequest.objects.get(id=request_id)
    admin_request.status = "rejected"
    admin_request.save()
    messages.success(request, "Request rejected!")
    return redirect("admin:manage_admin_requests")
