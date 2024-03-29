from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Messagem', widget=forms.Textarea())

    # def __init__(self,*args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['message'].widget.attrs['class'] = 'form-control'

    def send_mail(self):
        nome = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = f"Nome: {nome}\nE-mail: {email}\n{message}"
        send_mail('Contato E-commerce', message, settings.DEFAULT_FROM_EMAIL,[settings.DEFAULT_FROM_EMAIL])
