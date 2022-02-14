from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .forms import DeliveryForm
from datetime import date 
from .models import *

# Create your views here.
class DeliveryUpdate(UpdateView):
    model = Delivery_Address
    fields = '__all__'

def home(request):
    return render(request, 'home.html')

def cart_index(request):
    cart = Cart.objects.get(user = request.user)
    donuts = cart.donuts.all()
    checkout = True 
    confirm = False
    order = 0
    print(request.path_info)
    if request.path_info == '/cart/review/':
        confirm = True
    if request.path_info == '/cart/complete/':
        checkout = False 
        order = Order(
            order_no=1000, 
            delivery_date= date.today(), 
            user = request.user, 
        )
        order.save()
        for donut in donuts:
            order.donuts.add(donut)
        order.save()
    return render(request,'cart/index.html', {
        'cart': cart, 
        'donuts': donuts,
        'confirm': confirm,
        'checkout': checkout,
        'order': order
    })

def cart_payment(request):
    cart = Cart.objects.get(user = request.user)
    donuts = cart.donuts.all()
    delivery_form = DeliveryForm()
    return render(request,'cart/payment.html', {
        'donuts': donuts, 
        'delivery_form': delivery_form
    })

def add_info(request):
    form = DeliveryForm(request.POST)
    profile = request.user.profile_set.first()
    if form.is_valid():
        delivery_address = form.save(commit=False)
        delivery_address.profile_id = profile.id
        delivery_address.save()
    return redirect('cart_review')

def donuts_index(request):
    donuts = Donut.objects.all()
    return render(request, 'donuts/index.html', {'donuts': donuts})

def donut_detail(request, donut_id):
    donut = Donut.objects.get(id=donut_id)
    return render(request, 'donuts/detail.html',{'donut': donut})
    
def add_donut_cart(request, donut_id):
    donut = Donut.objects.get(id = donut_id)
    cart = Cart.objects.get(user = request.user)
    cart.donuts.add(donut)
    return redirect('detail', donut_id= donut_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      Profile(rewards=0, user = user).save()
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
