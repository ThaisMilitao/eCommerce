from django.db import models
from django.core import validators 
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, UserManager
import re

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Username', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .'
                , 'invalid'
            )
        ], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
    )
    name = models.CharField('Name', max_length=100, blank=True)
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Is staff', default=False)
    is_active = models.BooleanField('Is active', default=True)
    date_joined = models.DateTimeField('Date joined', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    # class Meta:
    #     verbose_name = 'Usúario'
    #     verbose_name_plural = 'Usúarios' 
        
    def __str__(self):
        return self.name or self.username
    
    def get_full_name(self):
        return str(self)
    
    def get_short_name(self):
        return str(self).split(" ")[0]
    