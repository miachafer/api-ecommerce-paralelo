from rest_framework import serializers
from .models import Order, Item

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    """
    The following function validate if the order's description contains letters. If the description doesn't contain a single letter, these function will raise an error.
    """
    def validate_description(self, description):
        is_there_a_letter = any(c.isalpha() for c in description)
        if is_there_a_letter == False:
            raise serializers.ValidationError("The order's description must contain letters.")
        return description

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
