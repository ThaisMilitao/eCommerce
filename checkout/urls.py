from . import views
from django.urls import path

app_name='checkout'
urlpatterns = [
    path('cartItem/add/<slug>',views.createCartItem, name='create_cartitem'),
    path('cartItem',views.cartItem, name='cart_item'),
    path('checkout',views.checkout, name='checkout'),

]
