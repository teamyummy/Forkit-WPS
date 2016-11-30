from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer
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
        pk = self.kwargs['pk']
        restaurant = get_object_or_404(Restaurant, pk=pk)
        return Menu.objects.filter(restaurant=restaurant)

#    def list(self, request, *args, **kwargs):
#        pk = kwargs['pk']
#        queryset = self.get_queryset()
#        queryset.filter(restaurant=pk)
#        serializer = 


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


