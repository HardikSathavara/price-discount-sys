from rest_framework import serializers
from .models import Product, Discount, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    discounts = serializers.PrimaryKeyRelatedField(many=True, queryset=Discount.objects.all())
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'items', 'discounts', 'total']

    def get_total(self, obj):
        return obj.calculate_total()

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        discounts = validated_data.pop('discounts')
        order = Order.objects.create(**validated_data)
        order.discounts.set(discounts)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order