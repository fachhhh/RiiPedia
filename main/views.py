from django.shortcuts import render

def show_main(request):
    context = {
        'ecommerce' : 'RiiPedia',
        'name' : 'Hadyan Fachri',
        'npm' : '2306245030',
        'class' : 'PBP A',
        'productname' : 'Chainsaw Man 1 (Japanese Version)',
        'price' : '121000',
        'quantity' : '30',
        'description' :'Shounen manga by Tatsuki Fujimoto',
    }

    return render(request, "main.html", context)