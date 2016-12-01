from .models import MyUser
from rest_framework import serializers
from dining.models import Restaurant, Menu, Review


class MyUserSerializer(serializers.ModelSerializer):
    restaurants = serializers.PrimaryKeyRelatedField(many=True, queryset=Restaurant.objects.all())

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'restaurants')
