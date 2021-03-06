from venv import create
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import DeliveryForm, UserForm
from datetime import date 
from .models import *

# Create your views here.
class DeliveryUpdate(UpdateView):
    model = Delivery_Address
    fields = ['address', 'apartment','city','country','Province', 'postal_code']


def home(request):
    donuts = Donut.objects.all()
    return render(request, 'home.html', {
        'donuts': donuts,
    })

@login_required
def cart_index(request):
    user = request.user
    cart = Cart.objects.get(user = user)
    user_items = cart.itemcart_set.all()
    profile = Profile.objects.get(user = user)
    address = ''
    print(address)
    checkout = True 
    confirm = False
    order = 0
    today = date.today()
    print(request.path_info)
    if request.path_info == '/cart/review/':
        address = Delivery_Address.objects.get(profile = profile)
        print(cart.date)
        confirm = True
        checkout = False
    if request.path_info == '/cart/complete/':
        address = Delivery_Address.objects.get(profile = profile)
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
        cart.save()
    return render(request,'cart/index.html', {
        'cart': cart, 
        'items': user_items,
        'confirm': confirm,
        'checkout': checkout,
        'order': order,
        'address': address,
        'user': user,
        'today': today,
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
    print(len(cart.donuts.all()))
    if len(cart.donuts.all()) < 1:
        return redirect('cart')
    if request.POST:
        cart.date = request.POST['date']
        cart.notes = request.POST['notes']
        cart.save()
    user_items = cart.itemcart_set.all()
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
        'items': user_items, 
        'delivery_form': delivery_form,
        'address': address
    })

@login_required
def account_profile(request):
    orders = request.user.order_set.all()
    profile=Profile.objects.get(user=request.user)
    delivery_address=''
    try:
        delivery_address=Delivery_Address.objects.get(profile=profile)
    except:
        print('error')
    return render(request, 'profile/index.html', {
        'orders': orders, 
        'profile':profile,
        'user': request.user,
        'delivery_address': delivery_address})

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
    added = False 
    try:
        if Cart.objects.get(donuts = donut):
            added = True
    except:
        print('error')
    return render(request, 'donuts/detail.html',{'donut': donut, 'added': added})

@login_required
def quick_add(request,donut_id):
    donut = Donut.objects.get(id = donut_id)
    cart = Cart.objects.get(user = request.user)
    cart.donuts.add(donut)
    return redirect('shop')

@login_required    
def add_donut_cart(request, donut_id):
    donut = Donut.objects.get(id = donut_id)
    cart = Cart.objects.get(user = request.user)
    cart.donuts.add(donut)
    if donut.special:
        return redirect('daily_flavour')
    else:
        return redirect('detail', donut_id= donut_id)

@login_required
def delete_donut (request, donut_id):
    donut = Donut.objects.get(id = donut_id)
    cart = Cart.objects.get(user = request.user)
    cart.donuts.remove(donut)
    return redirect('cart')

@login_required
def add_review(request, donut_id):
    donuts = Donut.objects.get(id=donut_id)
    print(request.POST)
    Review.objects.create(
        content= request.POST['review_text'], 
        rating= request.POST['rating'] if request.POST['rating'] else 5, 
        donuts=donuts, 
        user=request.user)
    return redirect('detail', donut_id=donut_id)

def signup(request):
  error_message = ''
  errors = ''
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      Profile(rewards=0, user = user).save()
      Cart(user=user, date= date.today()).save()
      return redirect('home')
    else:
      errors=form.errors
      error_message = 'Invalid sign up - try again'
      print(errors)
  form = UserForm()
  context = {'form': form, 'error_message': error_message, 'errors':errors}
  return render(request, 'registration/signup.html', context)

@login_required
def quantity_update(request, donut_id, item_id, amount_id):
    item = ItemCart.objects.get(id= item_id)
    item.quantity = int(amount_id)
    item.save()
    response = HttpResponse("done")
    return response 

def add_note(request):
    pass

def daily_flavour(request):
    donuts = Donut.objects.filter(special='True')
    oddIndexes = range(1, 10000, 2)
    evenIndexes = range(0, 10000, 2)
    return render(request,'daily/index.html', {'donuts': donuts, 'oddIndexes': oddIndexes, 'evenIndexes': evenIndexes})

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched'].lower()
        donuts = Donut.objects.filter(description__icontains=searched)
        return render(request, 'donuts/index.html', {'searched': searched, 'donuts': donuts })
    else:
        donuts = Donut.objects.all()
        return render(request, 'donuts/index.html', {'donuts': donuts})

def faq(request):
    return render(request, 'faq/index.html')

def rewards(request):
    return render(request, 'rewards/index.html')

def about(request):
    return render(request, 'about/index.html')