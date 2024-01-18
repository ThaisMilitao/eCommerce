from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import TemplateView
from django.contrib import messages

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    
home = IndexView.as_view()

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Form Invalid')
    context={
        'form':form,
        'success': success,
    }
    return render(request, 'contact.html', context)