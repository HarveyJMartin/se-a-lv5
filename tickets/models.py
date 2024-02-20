from django.db import models
from django.contrib.auth.models import User
from devices.models import devices
from django.utils import timezone
from datetime import timedelta


# Create your models here.
class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='customer_tickets')
    device = models.ForeignKey(devices, on_delete=models.CASCADE, blank=True)
    resolved = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_tickets')
    created_date = models.DateTimeField(auto_now_add=True)
    expected_resolution_date = models.DateTimeField(null=True, blank=True)
    closed_date = models.DateTimeField(null=True, blank=True)
    

    def set_closed_date(self):
        if self.resolved and not self.closed_date:
            self.closed_date = timezone.now()
        elif not self.resolved:
            self.closed_date = None

        super(Ticket, self).save()


    def set_default_resolution(self):
            if not self.expected_resolution_date:
                # If expected_resolution_date is not set, calculate it
                self.expected_resolution_date = self.created_date + timedelta(days=3)
            super(Ticket, self).save()