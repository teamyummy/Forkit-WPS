from rest_framework import serializers
from .models import Restaurant, Menu, Review, RestaurantImg


class MenuSerializer(serializers.ModelSerializer):
    restaurant = serializers.ReadOnlyField(source="restaurant.name")
    # img_t = serializers.ReadOnlyField(source="img.thumbnail['200x200'].url")

    class Meta:
        model = Menu
        fields = ('id', 'restaurant', 'name', 'price', 'description', 'img')

    def to_representation(self, obj):
        ret = super().to_representation(obj)

        img_t = obj.img.thumbnail['200x10000'].url
        img_s = obj.img.thumbnail['400x10000'].url

        request = self.context.get('request', None)
        if request is not None:
            ret['img_t'] = request.build_absolute_url(img_t)
            ret['img_s'] = request.build_absolute_url(img_s)
        


class RestaurantImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantImg
        field = ('id', 'restaurant', 'img', 'alt')


class RestaurantSerializer(serializers.ModelSerializer):
    register = serializers.ReadOnlyField(source='register.username')
    menus = MenuSerializer(many=True, read_only=True)
    images = RestaurantImgSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'register', 'name', 'address', 'phone',
                  'latitude', 'longitude', 'description',
                  'can_parking', 'desc_parking', 'desc_delivery',
                  'operation_hour', 'review_count', 'review_score',
                  'total_like', 'created_date', 'menus', 'images',
                  )
