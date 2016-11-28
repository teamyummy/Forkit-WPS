from django.db import models
from django.contrib.auth.models import AbstractUser, UserManger
from versatileimagefield.fields import VersatileImageField


class MyUser(AbstractUser):
    profile_img = models.

