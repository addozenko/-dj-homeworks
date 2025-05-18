from django.shortcuts import render, redirect

from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET['sort']
    phones = {'name': Phone.objects.all().order_by('name'),
              'min_price': Phone.objects.all().order_by('-price'),
              'max_price' : Phone.objects.all().order_by('price'),}

    context = {'phones': phones[sort]}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.all().get(slug = slug)
    context = {'phone': phone}
    return render(request, template, context)
