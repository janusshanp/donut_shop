from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donut(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    special = models.BooleanField()
    image = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Cart(models.Model):
    donut_quantity = models.IntegerField()
    donut = models.ManyToManyField(Donut)

    def __str__(self):
        pass

class Review(models.Model):
    # CHOICES = [1,2,3,4,5]

    content = models.CharField(max_length=200)
    # rating = models.IntegerField(
    #     max_length=1,
    #     choices = CHOICES,
    #     default = CHOICES[4]
    # )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    donut = models.ForeignKey(Donut, on_delete=models.CASCADE)

class Orders(models.Model):
    order_no = models.IntegerField()
    delivery_date= models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Profile(models.Model):
    email = models.CharField(max_length=40)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Delivery_Address(models.Model):
    address = models.CharField(max_length=15)
    apartment = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    Province = models.CharField(max_length=15)
    postal_code = models.CharField(max_length=7)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)