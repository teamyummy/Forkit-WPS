from django.db import models
from django.conf import settings
from versatileimagefield.fields import VersatileImageField


class Restaurant(models.Model):
    register = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()

    can_parking = models.BooleanField()
    desc_parking = models.CharField(max_length=100)
    desc_delivery = models.CharField(max_length=100)
    operation_hour = models.CharField(max_length=100)

    review_count = models.IntegerField()
    review_score = models.FloatField()
    total_like = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    img = VersatileImageField('Image', upload_to='menu_imgs')


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(Restaurant)
    title = models.CharField(max_length=100)
    content = models.TextField()
    review_score = models.IntegerField()
    review_like = models.IntegerField()
    review_dislike = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)


class Restaurant_favor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(Restaurant)
    created_date = models.DateTimeField(auto_now_add=True)


class Restaurant_img(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    img = VersatileImageField('RestaurantImage', upload_to='restaurant_imgs')
    alt = models.CharField(max_length=100)


class Review_like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    review = models.ForeignKey(Review)
    up_and_down = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    

class Review_img(models.Model):
    review = models.ForeignKey(Review)
    img = VersatileImageField('ReviewImage', upload_to='review_imgs')
    alt = models.CharField(max_length=100)


