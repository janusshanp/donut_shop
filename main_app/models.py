from django.db import models
from django.contrib.auth.models import User


CHOICES = (
    ('1', 'One Star'),
    ('2', 'Two Star'),
    ('3', 'Three Star'),
    ('4', 'Four Star'),
    ('5', 'Five Star'),
)
# Create your models here.
class Donut(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    special = models.BooleanField()
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_no = models.IntegerField()
    delivery_date= models.DateTimeField()
    ordered_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    donuts = models.ManyToManyField(Donut)

    def __str__(self):
        return f"No. {self.order_no}"


class Cart(models.Model):
    donuts = models.ManyToManyField(
        Donut,
        through ='ItemCart',
        through_fields=('cart', 'donut')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField('order date')
    
    def __str__(self):
        return f"{self.user}"

class ItemCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    donut = models.ForeignKey(Donut, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        default=1
    )

    def __str__(self):
        return f"Cart {self.cart}'s Items with {self.donut}"

class Review(models.Model):
    content = models.CharField(max_length=200)
    rating = models.CharField(
        max_length= 1,
        choices = CHOICES,
        default = CHOICES[4][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    donuts = models.ForeignKey(Donut, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s {self.donuts} Review"

class Profile(models.Model):
    rewards = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s Profile"

class Delivery_Address(models.Model):
    email = models.CharField(max_length=25)
    address = models.CharField(max_length=15)
    apartment = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    Province = models.CharField(max_length=15)
    postal_code = models.CharField(max_length=7)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile}'s Delivery Address" 