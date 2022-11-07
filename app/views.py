from django.shortcuts import render
from django.http import JsonResponse
from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
# @api_view(['GET'])
def getRoutes(request):
    return JsonResponse('Hello', safe=False)

@api_view(['GET'])
def getProducts(request):
    return Response(products)

@api_view(['GET'])
def getProduct(request,pk):
    product = None
    # get a single product first loop through all products
    for i in products:
        if i ['_id'] == pk:
            product = i
            break
        
    return Response(product)


