from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from admin.models import AdminRequest
from django.db import transaction
from django import forms


class SignUpForm(UserCreationForm):
    request_admin = forms.BooleanField(required=False, label="Request admin access")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "request_admin")

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            if self.cleaned_data.get("request_admin", False):
                AdminRequest.objects.create(user=user)
        return user
