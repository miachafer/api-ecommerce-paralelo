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
    
    """
    The following function returns the full data of an order.
    """
    def retrieve(self, request,  pk="id"):
        try:
            order = self.get_object()
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"Error": str(e)})

        order_helper = OrderHelper(order)
        order_details = order_helper.checking_order()

        if not order_details:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"Error": "Order is empty. Add items."})

        return Response(status=status.HTTP_200_OK, data={'order_details': order_details})

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    """
    The following function updates the quantity of products when a item is created. If the quantity of items is bigger than the quantity of products, function gets a 400 status.
    """
    def create(self, request):   
        item = self.serializer_class(data=request.data)
        if item.is_valid():
            item_quantity = request.data['quantity']
            product = Product.objects.get(id=request.data['product'])
            product_quantity = product.quantity
            
            if int(item_quantity) > int(product_quantity):
                return Response({"status": "Error", "data": "This product is not available in stock or you must try a smaller amount of it."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                product.quantity = product.quantity - int(request.data['quantity'])
                product.save()
                item.save()
                return Response({"data": item.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "Error", "data": "Invalid data. Check if the quantity field is not blank."}, status=status.HTTP_400_BAD_REQUEST)

