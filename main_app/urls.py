from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.donuts_index, name='shop'),
    path('shop/<int:donut_id>/', views.donut_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('cart/', views.cart_index, name="cart"),
    path('cart/<int:donut_id>/', views.add_donut_cart, name="add_cart"),
    path('cart/payment/', views.cart_payment, name="payment"),
    path('cart/payment/info/', views.add_info, name= "add_info"),
    path('cart/review/',views.cart_index, name="cart_review"),
    path('cart/complete', views.cart_index, name="cart_complete"),
]