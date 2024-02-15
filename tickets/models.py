from django.db import models

# Create your models here.
class Ticket(models.Model):
    ID = models.AutoField(primary_key=True)
    Device = models.CharField(max_length=100)
