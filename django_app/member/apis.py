from rest_framework import generics
from .serializers import MyUserSerializer
from .models import MyUser


class UserList(generics.ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
