from django import forms
from .models import AdminRequest

class AdminRequestForm(forms.ModelForm):
    class Meta:
        model = AdminRequest
        fields = []  # specify fields if needed, or leave empty to use all fields from the model
