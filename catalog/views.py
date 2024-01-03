from django.shortcuts import render
from .models import Product, Category
from .forms import ContactForm

# Create your views here.
def products_list(request):
    template_name = 'products.html'
    products = Product.objects.all()
    context = {
        'products': products,
    }   
    return render(request,template_name, context)


def category_products(request, slug):
    template_name = 'category_products.html'
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    context = {
        'current_category':category,
        'products': products,

    }   
    return render(request,template_name, context)

def home(request):
    return render(request, 'index.html')

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True

    context={
        'form':form,
        'success': success,
    }
    return render(request, 'contact.html', context)

def product(request,slug):
    template_name = 'product.html'
    product = Product.objects.get(slug=slug)
    context = {
        'product': product,
    }   
    return render(request,template_name, context)
