from django.shortcuts import render, get_object_or_404, redirect
from .models import devices
from django.contrib.auth.decorators import login_required
from ticket_app.decorators import admin_required
from .forms import DeviceForm
# Create your views here.


@login_required
def all_devices(request):
    device = devices.objects.all()
    return render(request, 'all_devices.html', {'devices': device})

@admin_required
def create_device(request):
    if request.method == 'POST':
        # If it's a POST request, create a form instance with the POST data
        form = DeviceForm(request.POST)
        if form.is_valid():
            # Save the form and redirect to the all_devices view
            form.save()
            return redirect('/devices/')
    else:
        # If it's a GET request, create an empty form
        form = DeviceForm()

    return render(request, 'create_device.html', {'form': form})


@admin_required
def edit_device(request, pk):
    # Fetch the device object by its primary key (pk)
    device = get_object_or_404(devices, pk=pk)
    
    if request.method == 'POST':
        # Populate the form with the POST data and the instance of the device
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            # Save the form and redirect to the all_devices view
            form.save()
            return redirect('/devices/')
    else:
        # If it's a GET request, populate the form with the instance of the device
        form = DeviceForm(instance=device)

    return render(request, 'edit_device.html', {'form': form, 'device': device})
    

@admin_required
def delete_device(request, pk):
    # Fetch the device object by its primary key (pk)
    device = get_object_or_404(devices, pk=pk)
    
    if request.method == 'POST':
        # Delete the device object and redirect to the all_devices view
        device.delete()
        return redirect('/devices/')
    
    return render(request, 'delete_device.html', {'device': device})
