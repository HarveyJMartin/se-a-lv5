from django import forms
from .models import Ticket


class BaseTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["device", "comments"]

    def clean(self):
        cleaned_data = super().clean()
        comments = cleaned_data.get("comments")
        device = cleaned_data.get("device")

        if not comments:
            raise forms.ValidationError("Comments cannot be empty.")
        if not device:
            raise forms.ValidationError("Device cannot be empty.")

        return cleaned_data


class FullTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "customer",
            "device",
            "resolved",
            "assigned_to",
            "expected_resolution_date",
            "closed_date",
        ]


class CreateTicketForm(BaseTicketForm):
    pass  # Inherits everything from BaseTicketForm


class EditTicketForm(BaseTicketForm):
    pass  # Inherits everything from BaseTicketForm
