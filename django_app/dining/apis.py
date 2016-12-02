from .models import Restaurant, Menu, Review
from .models import RestaurantImg, RestaurantTag, ReviewImg
from .models import RestaurantFavor
from .serializers import RestaurantSerializer, MenuSerializer
from .serializers import RestaurantImgSerializer
from .serializers import ReviewSerializer, TagSerializer
from .serializers import FavorSerializer
from .serializers import ReviewImgSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions


class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(register=self.request.user)


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return Menu.objects.filter(restaurant=restaurant)

    def perform_create(self, serializer):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        serializer.save(restaurant=restaurant)

#    def list(self, request, *args, **kwargs):
#        pk = kwargs['pk']
#        queryset = self.get_queryset()
#        queryset.filter(restaurant=pk)
#        serializer = 


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return Menu.objects.filter(restaurant=restaurant)


class RestaurantImgList(generics.ListCreateAPIView):
    queryset = RestaurantImg.objects.all()
    serializer_class = RestaurantImgSerializer

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return RestaurantImg.objects.filter(restaurant=restaurant)

    def perform_create(self, serializer):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        serializer.save(restaurant=restaurant)


class RestaurantImgDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantImg.objects.all()
    serializer_class = RestaurantImgSerializer

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return RestaurantImg.objects.filter(restaurant=restaurant)


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return Review.objects.filter(restaurant=restaurant)

    def perform_create(self, serializer):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        review = serializer.save(author=self.request.user, restaurant=restaurant)
        restaurant.review_count += 1
        restaurant.review_score += review.score
        restaurant.save()


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return Review.objects.filter(restaurant=restaurant)


class TagList(generics.ListCreateAPIView):
    queryset = RestaurantTag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return RestaurantTag.objects.filter(restaurant=restaurant)

    def perform_create(self, serializer):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        serializer.save(restaurant=restaurant)


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantTag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return RestaurantTag.objects.filter(restaurant=restaurant)


class FavorList(generics.ListCreateAPIView):
    queryset = RestaurantFavor.objects.all()
    serializer_class = FavorSerializer

    def get_queryset(self):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        return RestaurantFavor.objects.filter(restaurant=restaurant)

    def perform_create(self, serializer):
        rest_id = self.kwargs['rest_id']
        restaurant = get_object_or_404(Restaurant, pk=rest_id)
        serializer.save(author=self.request.user, restaurant=restaurant)
        restaurant.total_like += 1
        restaurant.save()


class FavorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantFavor.objects.all()
    serializer_class = FavorSerializer



class ReviewImgList(generics.ListCreateAPIView):
    queryset = ReviewImg.objects.all()
    serializer_class = ReviewImgSerializer

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        review = get_object_or_404(Review, pk=review_id)
        return ReviewImg.objects.filter(review=review)

    def perform_create(self, serializer):
        review_id = self.kwargs['review_id']
        review = get_object_or_404(Review, pk=review_id)
        serializer.save(review=review)
    

class ReviewImgDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewImg.objects.all()
    serializer_class = ReviewImgSerializer

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        review = get_object_or_404(Review, pk=review_id)
        return ReviewImg.objects.filter(review=review)


