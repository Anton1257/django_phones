from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def catalog_view(request):
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'name':
        phones = Phone.objects.order_by('name')
    elif sort_by == 'min_price':
        phones = Phone.objects.order_by('price')
    else:
        phones = Phone.objects.all()
    return render(request, 'catalog.html', {'phones': phones})


def product_view(request, slug):
    phone = Phone.objects.get(slug=slug)
    return render(request, 'product.html', {'phone': phone})
