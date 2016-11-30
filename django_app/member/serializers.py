from rest_framework import serializers
from dining.models import Restaurant
from .models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    restaurants = serializers.PrimaryKeyRelatedField(
                        many=True, queryset=Restaurant.objects.all())

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'restaurants')

