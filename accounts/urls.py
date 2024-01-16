from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('',views.index, name='index'),
    path('register',views.register, name='register'),
    path('update-user',views.update_user, name='update_user'),
    path('update-password',views.update_password, name='update_password'),


]