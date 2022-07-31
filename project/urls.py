from django.contrib import admin
from django.urls import path, include
from project.client.views import ClientViewSet
from project.product.views import ProductViewSet
from project.order.views import  OrderViewSet, ItemViewSet
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register('clients', ClientViewSet)
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)
router.register('items', ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
