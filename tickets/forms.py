from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['customer', 'device', 'resolved', 'assigned_to', 'expected_resolution_date', 'closed_date']