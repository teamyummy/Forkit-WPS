from django.db import models
from django.contrib.auth.models import AbstractUser
from versatileimagefield.fields import VersatileImageField


class MyUser(AbstractUser):
    nickname = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
    profile_img = VersatileImageField(
                            'Profile',
                            upload_to='profile_imgs')


