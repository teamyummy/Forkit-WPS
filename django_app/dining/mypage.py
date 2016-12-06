from rest_framework import generics
from rest_framework import permissions
from .models import Restaurant, Review
from .serializers import RestaurantSerializer
from .serializers import ReviewSerializer


class MyRegisterRests(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Restaurant.objects.filter(register=self.request.user)


class MyFavorRests(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Restaurant.objects.filter(favors__user=self.request.user)


class MyAuthorReviews(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Review.objects.filter(author=self.request.user)


class MyLikeReviews(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Review.objects.filter(likes__user=self.request.user,
                                     likes__up_and_down__gt=0)


