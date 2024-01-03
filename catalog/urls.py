from . import views
from django.urls import path

app_name='catalog'
urlpatterns = [
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('product/<slug>',views.product, name='product'),
    path('products/',views.products_list, name='products_list'),
    path('categories/<slug>',views.category_products, name='category_products'),
]
