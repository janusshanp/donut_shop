from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.donuts_index, name='shop'),
    path('shop/<int:donut_id>/', views.donut_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('cart/', views.cart_index, name="cart"),
    path('cart/checkout', views.cart_checkout, name="checkout")
]