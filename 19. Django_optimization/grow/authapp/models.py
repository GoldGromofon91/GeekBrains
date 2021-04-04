import hashlib
from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from grow.settings import DOMAIN_NAME, EMAIL_HOST_USER, ACTIVATION_KEY_TTL


class GrowUser(AbstractUser):
    age_user = models.PositiveIntegerField('возраст', null=True)
    avatar_user = models.ImageField(upload_to='users_avatar', blank=True)
    activation_key = models.CharField(max_length=128, blank=True)
    user_activation_date = models.DateTimeField(auto_now_add=True, null=True)

    def basket_element_price(self):
        return sum(el.prod_cost for el in self.basket.all())

    def basket_element_count(self):
        return sum(el.count for el in self.basket.all())

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save(using=using)

    def generate_activation_key(self):
        salt = hashlib.sha256(self.username.encode("utf8")).hexdigest()[:6]
        self.activation_key = hashlib.sha256((self.email + salt).encode('utf8')).hexdigest()

    @property
    def is_activation_key_ttl_expired(self):
        return now() - self.user_activation_date > timedelta(hours=ACTIVATION_KEY_TTL)

    def send_user_confirm_email(self):
        verify_link = reverse('authapp:verify_user',
                              kwargs={'email': self.email,
                                      'activation_key': self.activation_key
                                      })
        subject = f'Здравствуйте, {self.username}! Подтвердите регистрацию!'
        message = f'Для регистрации аккаунта {self.username} на портале {DOMAIN_NAME}' \
                  f'Пройдите по ссылке {DOMAIN_NAME}{verify_link}'

        return send_mail(subject, message, EMAIL_HOST_USER, [self.email], fail_silently=False)
