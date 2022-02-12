from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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
    return render(request,'cart/payment.html')

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
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
