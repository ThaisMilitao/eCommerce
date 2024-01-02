from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')

def list_products(request):
    return render(request, 'products.html')