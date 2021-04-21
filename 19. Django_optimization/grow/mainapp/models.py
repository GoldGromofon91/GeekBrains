from django.db import models


# Create your models here.

class Users(models.Model):
    first_name = models.CharField('имя', max_length=50)
    last_name = models.CharField('фамилия', max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    password_hash = models.CharField('хеш-пароль', max_length=254)
    phone = models.IntegerField('телефон', default=0)

    def __str__(self):
        return f'{self.first_name} + {self.email}'


class GrowCategory(models.Model):
    name = models.CharField('категория товаров', max_length=50)
    description = models.CharField('описание', max_length=150, blank=True)
    is_active = models.BooleanField('активность', default=True)

    def __str__(self):
        return f'{self.name}'

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save(using=using)

    class Meta:
        verbose_name = 'категория продукта'
        verbose_name_plural = 'категории продукта'
        ordering = ['name']


class GrowProducts(models.Model):
    category = models.ForeignKey(GrowCategory, on_delete=models.CASCADE)
    name = models.CharField('имя товара', max_length=50)
    image = models.ImageField(upload_to='prod_img', blank=True)
    small_desc = models.CharField('краткое описание', max_length=150, blank=True)
    full_desc = models.TextField('полное описание', blank=True)
    price = models.DecimalField('цена', max_digits=8, decimal_places=2, default=0)
    count = models.PositiveIntegerField('количество на складе', default=0)
    is_active = models.BooleanField('активность', default=True)

    def __str__(self):
        return f'{self.name}({self.category.name})'

    @classmethod
    def get_items(cls):
        return cls.objects.filter(is_active=True,
                                  category__is_active=True)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
