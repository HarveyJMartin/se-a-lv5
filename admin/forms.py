from django import forms
from .models import AdminRequest


class AdminRequestForm(forms.ModelForm):
    class Meta:
        model = AdminRequest
        fields = []
