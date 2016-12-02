from rest_framework import serializers
from .models import Restaurant, Menu, Review
from .models import RestaurantImg, RestaurantTag, ReviewImg
from .models import RestaurantFavor


class ImageThumbMixin(object):

    def to_representation(self, obj):
        ret = super().to_representation(obj)

        if not hasattr(obj, 'img'):
            return ret

        img_t = obj.img.thumbnail['200x10000'].url
        img_s = obj.img.thumbnail['400x10000'].url

        request = self.context.get('request', None)
        if request is not None:
            ret['img_t'] = request.build_absolute_uri(img_t)
            ret['img_s'] = request.build_absolute_uri(img_s)

        return ret
    

class MenuSerializer(ImageThumbMixin, serializers.ModelSerializer):
    restaurant = serializers.ReadOnlyField(source='restaurant.name')
    #img_t = serializers.ReadOnlyField(source="img.thumbnail['200x200'].url")

    class Meta:
        model = Menu
        fields = ('id', 'restaurant',
                  'name', 'price', 'description', 'img')


class RestaurantImgSerializer(ImageThumbMixin, serializers.ModelSerializer):
    restaurant = serializers.ReadOnlyField(source='restaurant.name')

    class Meta:
        model = RestaurantImg
        fields = ('id', 'restaurant', 'img', 'alt')


class ReviewImgSerializer(ImageThumbMixin, serializers.ModelSerializer):
    review = serializers.ReadOnlyField(source='review.title')

    class Meta:
        model = ReviewImg
        fields = ('id', 'review', 'img', 'alt')


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    restaurant = serializers.ReadOnlyField(source='restaurant.name')
    images = ReviewImgSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'author', 'restaurant', 'title', 'content',
                  'score', 'like', 'dislike', 'created_date', 'images')


class TagSerializer(serializers.ModelSerializer):
    restaurant = serializers.ReadOnlyField(source='restaurant.name')

    class Meta:
        model = RestaurantTag
        fields = ('id', 'restaurant', 'name')


class FavorSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    restaurant = serializers.ReadOnlyField(source='restaurant.name')
    
    class Meta:
        model = RestaurantFavor
        fields = ('id', 'user', 'restaurant', 'created_date')


class RestaurantSerializer(serializers.ModelSerializer):
    register = serializers.ReadOnlyField(source='register.username')
#    menus = serializers.PrimaryKeyRelatedField(
#                    many=True, queryset=Menu.objects.all())
    menus = MenuSerializer(many=True, read_only=True)
    images = RestaurantImgSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'register',
                  'name', 'address', 'phone',
                  'latitude', 'longitude', 'description',
                  'can_parking', 'desc_parking', 'desc_delivery',
                  'operation_hour',
                  'review_count', 'review_score',
                  'total_like', 'created_date',
                  'menus', 'images', 'reviews', 'tags')


