import datetime
from django.shortcuts import render, redirect
from main.forms import EcommerceEntryForm
from main.models import Ecommerce
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required(login_url='/login')
def show_main(request):
    product_entries = Ecommerce.objects.all()
    context = {
        'ecommerce' : 'RiiPedia',
        'name' : 'Hadyan Fachri',
        'npm' : '2306245030',
        'class' : 'PBP A',
        'product_entries' : product_entries,
        'last_login' : request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = EcommerceEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form':form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Ecommerce.objects.all()

def show_xml(request):
    data = Ecommerce.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Ecommerce.objects.all()

def show_json(request):
    data = Ecommerce.objects.all()
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
        form = AuthenticationForm(request)
    context = {'form':form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

