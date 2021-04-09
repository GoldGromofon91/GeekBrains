from random import random

from django.core.management.base import BaseCommand

from authapp.models import GrowUser,GrowUserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        for user in GrowUser.objects.filter(growuserprofile__isnull=True):
            GrowUserProfile.objects.create(user=user)
