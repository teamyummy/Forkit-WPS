from django.db import models
from django.conf import settings
from versatileimagefield.fields import VersatileImageField
import os
from uuid import uuid4


def file_path(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(path, filename)
    return wrapper


class Restaurant(models.Model):
    register = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='restaurants')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()

    can_parking = models.BooleanField()
    desc_parking = models.CharField(max_length=100, blank=True)
    desc_delivery = models.CharField(max_length=100, blank=True)
    operation_hour = models.CharField(max_length=100, blank=True)

    review_count = models.IntegerField(default=0, db_index=True)
    review_score = models.IntegerField(default=0)
    review_average = models.FloatField(default=0, db_index=True)
    total_like = models.IntegerField(default=0, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.review_count == 0:
            self.review_average = 0
        else:
            self.review_average = self.review_score / self.review_count

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-pk']

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='menus')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    img = VersatileImageField('Image', upload_to=file_path('menu_imgs'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk']


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(Restaurant, related_name='reviews')
    title = models.CharField(max_length=100)
    content = models.TextField()
    score = models.IntegerField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pk']


class RestaurantTag(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='tags')
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("restaurant", "name")
        ordering = ['restaurant', 'name']


class RestaurantFavor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(Restaurant, related_name='favors')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "restaurant")
        ordering = ['pk']


class RestaurantImg(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='images')
    img = VersatileImageField('RestaurantImage',
                                upload_to=file_path('restaurant_imgs'))
    alt = models.CharField(max_length=100)

    class Meta:
        ordering = ['pk']


class ReviewLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    review = models.ForeignKey(Review, related_name='likes')
    up_and_down = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['pk']


class ReviewImg(models.Model):
    review = models.ForeignKey(Review, related_name='images')
    img = VersatileImageField('ReviewImage', upload_to=file_path('review_imgs'))
    alt = models.CharField(max_length=100)

    class Meta:
        ordering = ['pk']

