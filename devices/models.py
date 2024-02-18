from django.db import models

# Create your models here.
class devices(models.Model):
    id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=50)