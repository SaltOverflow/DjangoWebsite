from django.shortcuts import render

from .forms import ListingForm
from .models import Listing

# Create your views here.
def listings_view(request, *args, **kwargs):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings.html', context)

def listings_detail_view(request, id, *args, **kwargs):
    item = Listing.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, 'listings_detail.html', context)

def listings_create_view(request, *args, **kwargs):
    form = ListingForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ListingForm()

    context = {
        'form': form
    }
    return render(request, 'listings_create.html', context)