from django.contrib import admin
from clients.models import Client
# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'registration_date')
    search_fields = ('name', 'email')
    list_filter = ('registration_date',)
