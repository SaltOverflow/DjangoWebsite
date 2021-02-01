from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def info_view(request, *args, **kwargs):
    return render(request, 'info.html', {})


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})
