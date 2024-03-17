from django.db import models


# Create your models here.
class devices(models.Model):
    id = models.AutoField(primary_key=True)
    device_brand = models.CharField(max_length=50)
    device_model = models.CharField(max_length=50)

    OS_OPTIONS = [
        ("1", "Mac OS"),
        ("2", "Linux"),
        ("3", "Windows 10"),
        ("4", "Windows 11"),
        ("5", "IOS"),
    ]

    os_version = models.CharField(max_length=20, choices=OS_OPTIONS)

    def __str__(self):
        return f"{self.device_brand} - {self.device_model}"
