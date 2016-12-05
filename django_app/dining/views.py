from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .apis import RestaurantList, MenuList


def post_list(request):
    return render(request, 'dining/post_list.html', {})