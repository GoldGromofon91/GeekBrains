from django.contrib.auth.models import AbstractUser
from django.db import models


class GrowUser(AbstractUser):
    age_user = models.PositiveIntegerField('возраст',null=True)
    avatar_user = models.ImageField(upload_to='users_avatar', blank=True)
