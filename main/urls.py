from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, CartViewSet, ProductViewSet, CustomerViewSet

router = DefaultRouter()
router.register('product', CategoryViewSet)
router.register('carts', CartViewSet)
router.register('products', ProductViewSet)
router.register('customer', CustomerViewSet)


urlpatterns = [
    path('', include(router.urls))
]