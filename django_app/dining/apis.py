from .models import Restaurant, Menu, Review
from .models import RestaurantImg, RestaurantTag, ReviewImg
from .models import RestaurantFavor, ReviewLike
from .serializers import RestaurantSerializer, MenuSerializer
from .serializers import RestaurantImgSerializer
from .serializers import ReviewSerializer, TagSerializer
from .serializers import FavorSerializer
from .serializers import ReviewImgSerializer
from .serializers import LikeSerializer

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import filters
from rest_framework.serializers import ValidationError
from django.db.models import F
from .perms import IsOwnerOrReadOnly
from .pages import MyPagination
#from .fils import TagFilter


class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('name', 'address', 'tags__name')
    ordering_fields = ('pk', 'review_count', 'review_average', 'total_like')
    pagination_class = MyPagination

#    def get_queryset(self):
#        return Restaurant.objects.order_by((F('review_score')/F('review_count')).desc())
    def get_queryset(self):
        tag_str = self.request.query_params.get('tags', None)
        if tag_str is None:
            return Restaurant.objects.all()

        #tags = ['식당', '두부']
        tags = tag_str.split(',')
        return Restaurant.objects.filter(tags__name__in=tags).distinct()

    def perform_create(self, serializer):
        serializer.save(register=self.request.user)


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class CreateRestPermMixin(object):
    def create(self, request, *args, **kwargs):
        rest_id = self.kwargs['rest_id']
        obj = get_object_or_404(Restaurant, pk=rest_id)
        self.check_object_permissions(request, obj)
        self.restaurant = obj

        return super().create(request, *args, **kwargs)


class CreateReviewPermMixin(object):
    def create(self, request, *args, **kwargs):
        review_id = self.kwargs['review_id']
        obj = get_object_or_404(Review, pk=review_id)
        self.check_object_permissions(request, obj)
        self.review = obj

        return super().create(request, *args, **kwargs)


class MenuList(CreateRestPermMixin, generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return Menu.objects.filter(restaurant=restaurant)

    def perform_create(self, serializer):
        serializer.save(restaurant=self.restaurant)

#    def list(self, request, *args, **kwargs):
#        pk = kwargs['pk']
#        queryset = self.get_queryset()
#        queryset.filter(restaurant=pk)
#        serializer = 


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return Menu.objects.filter(restaurant=restaurant)


class RestaurantImgList(CreateRestPermMixin, generics.ListCreateAPIView):
    queryset = RestaurantImg.objects.all()
    serializer_class = RestaurantImgSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return RestaurantImg.objects.filter(restaurant=restaurant)

    def perform_create(self, serializer):
        serializer.save(restaurant=self.restaurant)


class RestaurantImgDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantImg.objects.all()
    serializer_class = RestaurantImgSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return RestaurantImg.objects.filter(restaurant=restaurant)


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return Review.objects.filter(restaurant=restaurant)

    def perform_create(self, serializer):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        review = serializer.save(author=self.request.user, restaurant=restaurant,
                                imgs=self.request.data.getlist('imgs'),
                                alts=self.request.data.getlist('alts'))

        restaurant.review_count += 1
        restaurant.review_score += review.score
        restaurant.save()


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        self.restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return Review.objects.filter(restaurant=self.restaurant)

    def perform_update(self, serializer):
        org_score = serializer.instance.score
        new_score = serializer.validated_data['score']
        
        if org_score == new_score:
            serializer.save()
            return

        self.restaurant.review_score -= org_score
        self.restaurant.review_score += new_score

        serializer.save()
        self.restaurant.save()

    def perform_destroy(self, instance):
        self.restaurant.review_count -= 1
        self.restaurant.review_score -= instance.score

        instance.delete()
        self.restaurant.save()
    

class TagList(CreateRestPermMixin, generics.ListCreateAPIView):
    queryset = RestaurantTag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return RestaurantTag.objects.filter(restaurant=restaurant)

    def perform_create(self, serializer):
        serializer.save(restaurant=self.restaurant)


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantTag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return RestaurantTag.objects.filter(restaurant=restaurant)


class FavorList(generics.ListCreateAPIView):
    queryset = RestaurantFavor.objects.all()
    serializer_class = FavorSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return RestaurantFavor.objects.filter(restaurant=restaurant)

    def perform_create(self, serializer):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        serializer.save(user=self.request.user, restaurant=restaurant)
        restaurant.total_like += 1
        restaurant.save()


class FavorDetail(generics.RetrieveDestroyAPIView):
    queryset = RestaurantFavor.objects.all()
    serializer_class = FavorSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        self.restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return RestaurantFavor.objects.filter(restaurant=self.restaurant)

    def perform_destroy(self, instance):
        self.restaurant.total_like -= 1

        instance.delete()
        self.restaurant.save()


class ReviewImgList(CreateReviewPermMixin, generics.ListCreateAPIView):
    queryset = ReviewImg.objects.all()
    serializer_class = ReviewImgSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        review = get_object_or_404(Review, pk=review_id)
        return ReviewImg.objects.filter(review=review)

    def perform_create(self, serializer):
        serializer.save(review=self.review)
    

class ReviewImgDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewImg.objects.all()
    serializer_class = ReviewImgSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        review = get_object_or_404(Review, pk=review_id)
        return ReviewImg.objects.filter(review=review)


class LikeList(generics.ListCreateAPIView):
    queryset = ReviewLike.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        review = get_object_or_404(Review, pk=review_id)
        return ReviewLike.objects.filter(review=review)
        
    def perform_create(self, serializer):
        review_id = self.kwargs['review_id']
        review = get_object_or_404(Review, pk=review_id)
        user = self.request.user

        if ReviewLike.objects.filter(user=user, review=review).exists():
            raise ValidationError( { "non_field_errors":
                    "[ Like(user[{}],review[{}]) already exists ]"
                    .format(user.username, review.title) })

        like = serializer.save(user=user, review=review)
        if like.up_and_down > 0:
            review.like += like.up_and_down
        else:
            review.dislike += -like.up_and_down
        
        review.save()


class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewLike.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        self.review = get_object_or_404(Review, pk=review_id)
        return ReviewLike.objects.filter(review=self.review)

    def perform_update(self, serializer):
        org_score = serializer.instance.up_and_down
        new_score = serializer.validated_data['up_and_down']
        
        if org_score == new_score:
            return

        if org_score > 0:
            self.review.like -= org_score
        else:
            self.review.dislike += org_score

        if new_score > 0:
            self.review.like += new_score
        else:
            self.review.dislike += -new_score

        serializer.save()
        self.review.save()
        
    def perform_destroy(self, instance):
        if instance.up_and_down > 0:
            self.review.like -= instance.up_and_down
        else:
            self.review.dislike += instance.up_and_down

        instance.delete()
        self.review.save()


