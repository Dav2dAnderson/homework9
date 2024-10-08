from rest_framework.serializers import ModelSerializer

from .models import *



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CustomerSerialier(ModelSerializer):
    class Meta:
        models = Customer
        fields = "__all__"


    