from django.contrib import admin
from .models import Order

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'client', 'order_date', 'status')
    search_fields = ('order_number', 'client__name')
    list_filter = ('status', 'order_date')
    autocomplete_fields = ('client', 'products')
