from django.db import models
from django.conf import settings
from versatileimagefield.fields import VersatileImageField


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

    review_count = models.IntegerField(default=0)
    review_score = models.IntegerField(default=0)
    total_like = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='menus')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    img = VersatileImageField('Image', upload_to='menu_imgs')


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(Restaurant, related_name='reviews')
    title = models.CharField(max_length=100)
    content = models.TextField()
    score = models.IntegerField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)


class RestaurantTag(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='tags')
    name = models.CharField(max_length=20)

    class Meta:
        unique_together = ("restaurant", "name")


class RestaurantFavor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(Restaurant, related_name='favors')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "restaurant")


class RestaurantImg(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='images')
    img = VersatileImageField('RestaurantImage', upload_to='restaurant_imgs')
    alt = models.CharField(max_length=100)


class ReviewLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    review = models.ForeignKey(Review, related_name='likes')
    up_and_down = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    

class ReviewImg(models.Model):
    review = models.ForeignKey(Review, related_name='images')
    img = VersatileImageField('ReviewImage', upload_to='review_imgs')
    alt = models.CharField(max_length=100)


