from django.contrib import admin

from main_app.models import Donut, Cart, Review, Orders, Profile, Delivery_Address

# Register your models here.
admin.site.register(Donut)
admin.site.register(Cart)
admin.site.register(Review)
admin.site.register(Orders)
admin.site.register(Profile)
admin.site.register(Delivery_Address)