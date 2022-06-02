from pyexpat import model
from attr import fields
from rest_framework import serializers
from app2.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"