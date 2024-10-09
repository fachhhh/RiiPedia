import datetime
from django.shortcuts import render, redirect
from main.forms import EcommerceEntryForm
from main.models import Ecommerce
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    context = {
        'ecommerce' : 'RiiPedia',
        'name' : request.user.username,
        'npm' : '2306245030',
        'class' : 'PBP A',
        'last_login' : request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = EcommerceEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {'form':form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Ecommerce.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Ecommerce.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Ecommerce.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Ecommerce.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect('main:show_main')
    
    # hati hati salah identasi
    context = {'form' : form}
    return render(request, 'register.html', context)

    
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error("Invalid username or password. Please try again.")
        
    else:
        form = AuthenticationForm(request)
    context = {'form':form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = Ecommerce.objects.get(pk = id)
    form = EcommerceEntryForm(request.POST or None, instance=product)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form':form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Ecommerce.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    try:
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        description = request.POST.get("description")
        
        # Validasi input
        if not all([name, price, quantity, description]):
            return JsonResponse({
                "status": False,
                "message": "Semua field harus diisi!"
            }, status=400)
        
        # Konversi price dan quantity ke integer
        try:
            price = int(price)
            quantity = int(quantity)
        except ValueError:
            return JsonResponse({
                "status": False,
                "message": "Price dan quantity harus berupa angka!"
            }, status=400)

        # Buat produk baru
        new_product = Ecommerce.objects.create(
            user=request.user,
            name=name,
            price=price,
            quantity=quantity,
            description=description
        )

        # Serialize produk untuk response
        return JsonResponse({
            "status": True,
            "message": "Product berhasil ditambahkan!",
            "product": {
                "id": str(new_product.id),
                "name": new_product.name,
                "price": new_product.price,
                "quantity": new_product.quantity,
                "description": new_product.description
            }
        }, status=201)

    except Exception as e:
        return JsonResponse({
            "status": False,
            "message": str(e)
        }, status=500)