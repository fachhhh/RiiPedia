from django.shortcuts import render, redirect
from main.forms import EcommerceEntryForm
from main.models import Ecommerce
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    product_entries = Ecommerce.objects.all()
    context = {
        'ecommerce' : 'RiiPedia',
        'name' : 'Hadyan Fachri',
        'npm' : '2306245030',
        'class' : 'PBP A',
        'product_entries' : product_entries
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