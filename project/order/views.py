from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order, Item
from .serializers import OrderSerializer, ItemSerializer
from .helpers import OrderHelper
from project.product.models import Product

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer    
    http_method_names = ['get', 'post', 'put', 'delete']
    
    # This function returns the full data of an order
    def retrieve(self, request,  pk='id'):
        try:
            order = self.get_object()
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'Error': str(e)})

        order_helper = OrderHelper(order)
        order_details = order_helper.checking_order()

        if not order_details:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'error': 'Order is empty.'})

        return Response(status=status.HTTP_200_OK, data={'order_details': order_details})

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    # This function goal is to update the quantity of products when a item is created.
    # If the quantity of items is bigger than the quantity of products, function gets a 400; else: item is created.
    def create(self, request):   
        item = self.serializer_class(data=request.data)
        if item.is_valid():
            item_quantity = request.data['quantity']
            product = Product.objects.get(id=request.data['product'])
            product_quantity = product.quantity
            
            if int(item_quantity) > int(product_quantity):
                return Response({"status": "Error", "data": "Try a smaller amount of products."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                product.quantity = product.quantity - int(request.data['quantity'])
                product.save()
                item.save()
                return Response({"data": item.data}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

