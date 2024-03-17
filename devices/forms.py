from django import forms
from .models import devices


class DeviceForm(forms.ModelForm):
    class Meta:
        model = devices
        fields = ["device_brand", "device_model", "os_version"]
