from django.db import models

# Create your models here.
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name