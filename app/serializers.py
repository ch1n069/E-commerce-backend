from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product



class UserProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    createdOn = serializers.SerializerMethodField(read_only=True)
    class Meta: 
        model = User
        
        fields = ['id','username', 'email','name', "createdOn"]
        
    def get_name(self , obj):
        name = obj.first_name
        if name == '':#if user has not set name use email instead
            name = obj.email
            
        return name
    def get_createdOn(self, obj):
        createdOn = obj.date_joined
        return createdOn
    
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        
        fields = '__all__'
    
    