from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'commerce'

urlpatterns = [
    path('',views.home, name='home'),
    path('login',LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='home'), name='logout'),
    # path('register',views.register, name='register'),
    path('contact/',views.contact, name='contact'),
]
