# Generated by Django 2.2 on 2021-01-31 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='growproducts',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена'),
        ),
    ]