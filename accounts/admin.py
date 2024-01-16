from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BasedUserAdmin
from .models import User
from .forms import UserAdminCreationForm
# Register your models here.
class  UserAdmin(BasedUserAdmin):
    add_form = UserAdminCreationForm 
    
    add_fieldsets = (
        (None, {
            "fields": (' username', 'email', 'password1','password2'),
        }),
    )
    
    fieldsets = (
        (None, {
            "fields": ('username', 'email'),
        }),
        ('informações Basicas', {
            "fields": ('name', 'last_login')
        }),
        ('permissoes', {
            "fields": ('is_active', 'is_staff', 'is_superuser', 'groups','user_permissions')
        }),
    )

    list_display = ['username', 'name', 'is_active', 'is_staff', 'date_joined']

admin.site.register(User, UserAdmin)   