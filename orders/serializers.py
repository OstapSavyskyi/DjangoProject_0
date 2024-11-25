from rest_framework import serializers
from .models import Order
from clients.serializers import ClientSerializer
from products.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_number', 'client', 'products', 'order_date', 'status']
