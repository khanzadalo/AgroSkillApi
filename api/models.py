from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from datetime import datetime


def get_superuser():
    user = User.objects.filter(is_superuser=True).first()
    return user


def product_image(instance, filename):
    return 'images/{0}.jpg'.format(instance.slug)


def user_images(instance, filename):
    date_time = datetime.now().strftime("%Y_%m_%d,%H:%M:%S")
    saved_file_name = instance.user.username + "-" + date_time + ".jpg"
    return 'profile/{0}/{1}'.format(instance.user.username, saved_file_name)


class Category(models.Model):
    photo = models.ImageField(upload_to='categories/', blank=True, null=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.id}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False, blank=False)
    discount = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    category = models.ManyToManyField(Category, related_name='products')
    is_available = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.SET(get_superuser))
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='user_images', default='profile/default/default.png')
    total_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name

    def add_amount(self):
        amount = self.product.price * self.quantity
        profile = self.user.profile
        profile.total_price = profile.total_price + amount
        profile.save()
        return True


@receiver(post_delete, sender=Profile)
def profile_image_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(True)


@receiver(post_delete, sender=Product)
def product_image_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(True)
