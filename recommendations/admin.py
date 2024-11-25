from django.contrib import admin
from .models import Recommendation
# Register your models here.


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('client', 'created_at')
    search_fields = ('client__name',)
    list_filter = ('created_at',)
    autocomplete_fields = ('client', 'recommended_products')
