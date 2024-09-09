from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Chainsaw Man 1 (Japanese Version)',
        'price' : '121.000',
        'quantity' : '30',
        'description' :'Shounen manga by Tatsuki Fujimoto'
    }

    return render(request, "main.html", context)