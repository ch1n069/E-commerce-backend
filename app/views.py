from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .products import products
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from .models import *
from .serializers import ProductSerializer , UserProfileSerializer, UserSerializerWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status
# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        
        data = super().validate(attrs)
        
        serializer = UserSerializerWithToken(self.user).data
        
        for k ,v in serializer.items():
            data[k] = v

        return data
        
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    
# @api_view(['GET'])
def getRoutes(request):
    return JsonResponse('Hello', safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    
    user =request.user
    serializer = UserProfileSerializer(user, many=False)
    return Response(serializer.data)

#get all users 

#user registration 
@api_view(['POST'])
def registerUser(request):
    
    try:
        data = request.data
        user = User.objects.create(
            first_name = data['name'],
            username = data['email'],
            email = data['email'],
            password = make_password(data['password'])


        )
        serializer = UserSerializerWithToken(user, many=False)
        
        return Response(serializer.data)
    except:
        message = {"detail" : "a user with that email already exists "}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

# END OF USER REGISTER VIEW 

#//////////////////////////////// users edit profile //////////////////////////////////


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    
    user =request.user
    serializer = UserSerializerWithToken(user, many=False)
    
    data = request.data #pulling out the data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    
    if data['password'] != "":
        user.password = make_password(data['password'])
    user.save()
    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAdminUser])
def getAllUsers(request):
    
    users = User.objects.all()
    serializer = UserSerializerWithToken(users, many=True)
    return Response(serializer.data)

#end of get all users
@api_view(['GET'])
def getProducts(request):
    
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request,pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


