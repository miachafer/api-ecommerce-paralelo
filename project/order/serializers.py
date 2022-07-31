from rest_framework import serializers
from .models import Order, Item
# from project.product.serializers import ProductSerializer
# from project.product.models import Product

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
    

    
    # def create(self, validated_data):
    #     products_data = validated_data.pop('products')
    #     order = Order.objects.create(**validated_data)
    #     for product_data in products_data:
    #         Product.objects.create(order=order, **product_data)
    #     return order

'''
{
        "id": 5,
        "products": [
            {
                "id": 2,
                "name": "Caneta",
                "description": "Caneta preta.",
                "price": 1,
                "quantity": 10 ### THIS CAN'T SHOW!
            },
            {
                "id": 3,
                "name": "Borracha",
                "description": "Borracha verde",
                "price": 2,
                "quantity": 10 ### THIS CAN'T SHOW!
            }
        ],
        "client": "11122233345"
    },
'''