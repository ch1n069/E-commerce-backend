from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product
from rest_framework_simplejwt.tokens import RefreshToken


class UserProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    createdOn = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)


    class Meta: 
        model = User
        
        fields = ['id','_id','username', 'email','name', "createdOn", 'isAdmin']
        
    def get_name(self , obj):
        name = obj.first_name
        if name == '':#if user has not set name use email instead
            name = obj.email
            
            
        return name
    def get_createdOn(self, obj):
        createdOn = obj.date_joined
        return createdOn
    
    def get__id(self , obj):
        _id  = obj.id 
        return _id
    
    def get_isAdmin(self , obj):
        
         
        isAdmin = obj.is_staff
        return isAdmin
        
            
            
class UserSerializerWithToken(UserProfileSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    
    class Meta:
        model = User
        fields = ['id','_id','username', 'email','name', "createdOn", 'isAdmin' , "token"]
        
    def get_token(self , obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        
        fields = '__all__'
    
    