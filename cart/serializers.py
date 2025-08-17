from rest_framework import serializers
from .models import CartItem, Cart

class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'amount', 'create_at', 'update_at', 'total_price']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.ReadOnlyField()
    class Meta:
        model = Cart
        fields = ['id', 'user', 'create_at', 'total_price', 'items']
