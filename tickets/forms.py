from django import forms
from .models import Ticket

class FullTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['customer', 'device', 'resolved', 'assigned_to', 'expected_resolution_date', 'closed_date']

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['customer', 'device']