# Generated by Django 2.2 on 2021-04-08 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_remove_growuser_user_activation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrowUserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(blank=True, choices=[('M', 'male'), ('F', 'female')], max_length=1, verbose_name='gender')),
            ],
        ),
    ]
