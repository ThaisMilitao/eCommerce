from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ContactForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    
home = IndexView.as_view()

class Login(TemplateView):
    template_name = 'login.html'
    
login = Login.as_view()

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

# class RegisterView(CreateView):
#     form_class = UserCreationForm
#     template_name = 'register.html'
#     model = get_user_model()
#     success_url = reverse_lazy('home')

# register = RegisterView.as_view()