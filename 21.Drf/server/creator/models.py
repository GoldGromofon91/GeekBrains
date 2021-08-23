from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    username = models.CharField(max_length=100,unique=True,null=False,blank=False)
    email = models.CharField(max_length=48,unique=True,null=False,blank=False)
    birthday_year = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.username


