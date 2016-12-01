from dining.models import Restaurant, Menu
from dining.serializers import RestaurantSerializer, MenuSerializer
from rest_framework import generics
from rest_framework import permissions
from django.shortcuts import get_object_or_404

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