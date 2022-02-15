from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.account_profile, name="account_profile"),
    path('shop/', views.donuts_index, name='shop'),
    path('shop/<int:donut_id>/', views.donut_detail, name='detail'),
    path('shop/review/<int:donut_id>/', views.add_review, name='add_review'),
    path('accounts/signup/', views.signup, name='signup'),
    path('cart/', views.cart_index, name="cart"),
    path('cart/quantity/<int:donut_id>/<int:item_id>/<int:amount_id>/',views.quantity_update, name="quantity"),
    path('cart/notes/', views.add_note, name="add_note"),
    path('cart/<int:donut_id>/', views.add_donut_cart, name="add_cart"),
    path('cart/delete/<int:donut_id>/', views.delete_donut, name="delete_donut"),
    path('cart/payment/', views.cart_payment, name="payment"),
    path('cart/payment/info/', views.add_info, name= "add_info"),
    path('cart/review/',views.cart_index, name="cart_review"),
    path('cart/complete/', views.cart_index, name="cart_complete"),
]