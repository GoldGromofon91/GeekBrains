# Generated by Django 3.1 on 2021-09-06 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('ref', models.CharField(blank=True, max_length=128, null=True)),
                ('users', models.ManyToManyField(related_name='user_to_project', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_todo', to='todo.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_todo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заметка',
                'verbose_name_plural': 'Заметки',
            },
        ),
    ]