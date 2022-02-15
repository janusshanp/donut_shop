from venv import create
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import DeliveryForm
from datetime import date 
from .models import *

# Create your views here.
class DeliveryUpdate(UpdateView):
    model = Delivery_Address
    fields = '__all__'

def home(request):
    return render(request, 'home.html')

@login_required
def cart_index(request):
    cart = Cart.objects.get(user = request.user)
    user_items = cart.itemcart_set.all()
    # for item in user_items:
    #     print(item.donut.name)
    #     print(item.quantity)
    # donuts = cart.donuts.all()
    checkout = True 
    confirm = False
    order = 0
    print(request.path_info)
    if request.path_info == '/cart/review/':
        confirm = True
        checkout = False
    if request.path_info == '/cart/complete/':
        checkout = False 
        num = create_order_no()
        order = Order(
            order_no= num, 
            delivery_date= cart.date, 
            ordered_date = date.today(),
            user = request.user, 
        )
        order.save()
        for item in user_items:
            order.donuts.add(item.donut)
        order.save()
        cart.donuts.clear()
        cart.date = date.today()
    return render(request,'cart/index.html', {
        'cart': cart, 
        'items': user_items,
        'confirm': confirm,
        'checkout': checkout,
        'order': order
    })
def create_order_no():
    if Order.objects.last():
        num = Order.objects.last()
        num.order_no += 1
        return num.order_no
    else:
        return 1000

@login_required
def cart_payment(request):
    cart = Cart.objects.get(user = request.user)
    cart.date = request.POST['date']
    cart.save()
    donuts = cart.donuts.all()
    if request.user.profile_set.first().delivery_address_set.first():
        address = request.user.profile_set.first().delivery_address_set.first()
        delivery_form = DeliveryForm(initial= {
            'email': address.email,
            'address': address.address,
            'apartment': address.apartment,
            'city': address.city,
            'country': address.country,
            'Province': address.Province,
            'postal_code': address.postal_code
        })
    else:
        delivery_form = DeliveryForm()
        address = 0
    return render(request,'cart/payment.html', {
        'donuts': donuts, 
        'delivery_form': delivery_form,
        'address': address
    })

@login_required
def account_profile(request):
    orders = request.user.order_set.all()
    print(orders)
    return render(request, 'profile/index.html', {'orders': orders})

@login_required
def add_info(request):
    profile = request.user.profile_set.first()
    if request.user.profile_set.first().delivery_address_set.first():
        address = request.user.profile_set.first().delivery_address_set.first()
        data = {
            'email': address.email,
            'address': address.address,
            'apartment': address.apartment,
            'city': address.city,
            'country': address.country,
            'Province': address.Province,
            'postal_code': address.postal_code
        }
        form = DeliveryForm(request.POST, initial=data)
        if form.has_changed():
            if form.is_valid():
                delivery_address = form.save(commit=False)
                delivery_address.profile_id = profile.id
                delivery_address.save()
    else:
        form = DeliveryForm(request.POST)
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

def delete_donut (request, donut_id):
    donut = Donut.objects.get(id = donut_id)
    cart = Cart.objects.get(user = request.user)
    cart.donuts.remove(donut)
    return redirect('cart')

def add_review(request, donut_id):
    comment =request.POST['review_text']
    donuts = Donut.objects.get(id=donut_id)
    Review.objects.create(content=comment, rating=0, donuts=donuts, user=request.user)
    return redirect('detail', donut_id=donut_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      Profile(rewards=0, user = user).save()
      Cart(user=user, date= date.today()).save()
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
