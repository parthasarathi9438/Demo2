from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from app2.serializers import ProductSerializer, Product
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class InsertProduct(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

class ViewProduct(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class DeleteProduct(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]


class UpdateProduct(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]