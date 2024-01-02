from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('product/',views.product, name='product'),
    path('list_products/',views.list_products, name='list_products'),
]
