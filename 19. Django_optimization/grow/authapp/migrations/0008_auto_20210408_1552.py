# Generated by Django 2.2 on 2021-04-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20210408_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='growuserprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'male'), ('F', 'female')], max_length=1, verbose_name='gender'),
        ),
    ]
