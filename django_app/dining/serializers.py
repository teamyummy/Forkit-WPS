from rest_framework import serializers
from .models import Restaurant, Menu, Review

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'register',
                  'name', 'address', 'phone',
                  'latitude', 'longitude', 'description',
                  'can_parking', 'desc_parking', 'desc_delivery',
                  'operation_hour',
                  'review_count', 'review_score',
                  'total_like', 'created_date')

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'restaurant',
                  'name', 'price', 'description', 'img')

