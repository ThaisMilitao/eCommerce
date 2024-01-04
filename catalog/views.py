from typing import Any
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

from django.views import generic

# Create your views here.

class ProductListView(generic.ListView):
    model = Product
    template_name = 'products.html'
    context_object_name='products'

class CategoryListView(generic.ListView):
    template_name = 'category_products.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context
    

products_list = ProductListView.as_view()
category_products = CategoryListView.as_view()

def product(request,slug):
    template_name = 'product.html'
    product = Product.objects.get(slug=slug)
    context = {
        'product': product,
    }   
    return render(request,template_name, context)
