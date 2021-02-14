from django.shortcuts import render

from .forms import ContactForm
from .models import ContactInfo

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def info_view(request, *args, **kwargs):
    return render(request, 'info.html', {})


# def contact_view(request, *args, **kwargs):
#     form = ContactForm(request.POST or None)
#     submitted = False
#     if form.is_valid():
#         form.save()
#         submitted = True
#
#     context = {
#         'form': form,
#         'submitted': submitted
#     }
#     print(context)
#     return render(request, 'contact.html', context)
def contact_view(request, *args, **kwargs):
    form = ContactForm(request.POST or None)
    submitted = False
    if form.is_valid():
        form.save()
        form = ContactForm()
        submitted = True

    context = {
        'submitted': submitted,
        'form': form
    }
    return render(request, 'contact.html', context)
