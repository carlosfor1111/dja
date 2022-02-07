from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from base.models import Product
from base.products import products
from base.serializers import ProductSerializer
from rest_framework import status



@api_view(['GET', 'PUT', 'DELETE','POST'])
def getProducts(request):
    products = Product.objects.all()
    serialzer = ProductSerializer(products, many=True)
    return Response(serialzer.data)


@api_view(['GET', 'PUT', 'DELETE','POST'])
def getProduct(request , pk):
    product = Product.objects.get(id=pk)
    serialzer = ProductSerializer(product, many=False)
    return Response(serialzer.data)