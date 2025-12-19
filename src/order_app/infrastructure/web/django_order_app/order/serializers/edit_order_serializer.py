from rest_framework import serializers

from order_app.infrastructure.web.django_order_app.order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("product_id", "quantity")

    product_id = serializers.UUIDField()
    quantity = serializers.IntegerField(min_value=1)


class EditOrderRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("item",)

    item = OrderItemSerializer()
