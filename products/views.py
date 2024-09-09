from django.shortcuts import render, get_object_or_404
from .models import Product
from .serializers import Productserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

# Create your views here.

# @api_view(["GET","POST"])
# def product_list(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = Productserializer(products, many = True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = Productserializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=201)

# @api_view(["GET","PUT","DELETE"])
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'GET':
#         serializer = Productserializer(product)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = Productserializer(product, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#     elif request.method == "DELETE":
#         product.delete()
#         return Response(status=200)


class ProductListAPIView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = Productserializer(products, many=True)
        return Response(serializer.data)


class ProductCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = Productserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)


class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = Productserializer(product)
        return Response(serializer.data)

    def put(self, request, pk):

        product = self.get_object(pk)
        serializer = Productserializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):

        product = self.get_object(pk)
        product.delete()
        return Response(status=200)
