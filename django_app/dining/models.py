from django.db import models
from django.conf import settings


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








