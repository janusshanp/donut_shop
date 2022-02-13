from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import DeliveryForm
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def cart_index(request):
    cart = Cart.objects.get(user = request.user)
    donuts = cart.donuts.all()
    print(donuts)
    return render(request,'cart/index.html', {'cart': cart, 'donuts': donuts})

def cart_payment(request):
    cart = Cart.objects.get(user = request.user)
    donuts = cart.donuts.all()
    delivery_form = DeliveryForm()
    return render(request,'cart/payment.html', {'donuts': donuts, 'delivery_form': delivery_form})

def add_info(request):
    form = DeliveryForm(request.POST)
    # if form.is_valid():
    #     new_delivery_address
    return render(request, 'cart/review.html')

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
