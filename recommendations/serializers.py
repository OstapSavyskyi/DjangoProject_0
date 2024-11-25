from rest_framework import serializers
from .models import Recommendation
from clients.serializers import ClientSerializer
from products.serializers import ProductSerializer


class RecommendationSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    recommended_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Recommendation
        fields = ['id', 'client', 'recommended_products', 'created_at']
