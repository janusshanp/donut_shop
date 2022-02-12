from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.donuts_index, name='shop'),
    path('accounts/signup/', views.signup, name='signup'),
    path('cart/', views.cart_index, name="cart"),
]