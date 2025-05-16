from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, DiscountViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
