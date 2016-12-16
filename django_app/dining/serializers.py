from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Restaurant, Menu, Review
from .models import RestaurantImg, RestaurantTag, RestaurantFavor
from .models import ReviewImg, ReviewLike


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


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    review = serializers.ReadOnlyField(source='review.title')

    class Meta:
        model = ReviewLike
        fields = ('id', 'user', 'review', 'up_and_down', 'created_date')


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    rest_id = serializers.ReadOnlyField(source='restaurant.id')
    restaurant = serializers.ReadOnlyField(source='restaurant.name')
    images = ReviewImgSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'author', 'rest_id', 'restaurant', 'title', 'content',
                  'score', 'like', 'dislike', 'created_date', 'images')

    def create(self, validated_data):
        imgs = validated_data.pop('imgs')
        alts = validated_data.pop('alts')

        ris_list = []
        for img, alt in zip(imgs, alts):
            dict = { 'img':img, 'alt':alt }
            ris = ReviewImgSerializer(data=dict)
            ris.is_valid(raise_exception=True)
            ris_list.append(ris)

        ins = super().create(validated_data)
        for ris in ris_list:
            ris.save(review=ins)

        return ins

    def to_representation(self, obj):
        ret = super().to_representation(obj)

        request = self.context.get('request', None)
        ret['my_like'] = 0
        ret['my_like_id'] = 0
        if request is not None:
            if request.user.is_authenticated:
                try:
                    my_like = obj.likes.get(user=request.user)
                    ret['my_like'] = my_like.up_and_down
                    ret['my_like_id'] = my_like.pk
                except ObjectDoesNotExist:
                    pass

        return ret


class TagSerializer(serializers.ModelSerializer):
    restaurant = serializers.ReadOnlyField(source='restaurant.name')

    class Meta:
        model = RestaurantTag
        fields = ('id', 'restaurant', 'name')

    def validate(self, data):
        view = self.context['view']
        rest_id = view.kwargs['rest_id']
        name = data['name']

        if RestaurantTag.objects.filter(restaurant=rest_id, name=name).exists():
            raise serializers.ValidationError(
                    "Tag(restaurant,name[{}]) already exists".format(name))

        return data

class FavorSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    restaurant = serializers.ReadOnlyField(source='restaurant.name')
    
    class Meta:
        model = RestaurantFavor
        fields = ('id', 'user', 'restaurant', 'created_date')
#        validators = [
#            UniqueTogetherValidator(
#                queryset=RestaurantFavor.objects.all(),
#                fields=('user', 'restaurant')
#            )
#        ]

    def validate(self, data):
        #print('begin validate')

        request = self.context['request']
        view = self.context['view']

        user = request.user
        rest_id = view.kwargs['rest_id']

        if RestaurantFavor.objects.filter(user=user, restaurant=rest_id).exists():
            raise serializers.ValidationError("Favor(user,restaurant) already exists")

        return data


class RestaurantSerializer(serializers.ModelSerializer):
    register = serializers.ReadOnlyField(source='register.username')
#    menus = serializers.PrimaryKeyRelatedField(
#                    many=True, queryset=Menu.objects.all())
#    menus = MenuSerializer(many=True, read_only=True)
    menus = serializers.SerializerMethodField()
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
                  'review_count', 'review_score', 'review_average',
                  'total_like', 'created_date',
                  'menus', 'images', 'reviews', 'tags')

    def get_menus(self, obj):
#        q = obj.menus.all()[:3]
        q = obj.menus.all()
        s = MenuSerializer(q, many=True)
        return s.data

    def to_representation(self, obj):
        ret = super().to_representation(obj)

        request = self.context.get('request', None)

        ret['my_like'] = False
        ret['my_like_id'] = 0
        if request is not None:
            if request.user.is_authenticated:
                try:
                    my_like = obj.favors.get(user=request.user)
                    ret['my_like'] = True
                    ret['my_like_id'] = my_like.pk
                except ObjectDoesNotExist:
                    pass

        return ret

