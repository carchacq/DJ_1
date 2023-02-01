from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = Phone.objects.order_by("name")
    elif sort == 'min_price':
        phones = Phone.objects.order_by("price")
    elif sort == 'max_price':
        phones = Phone.objects.order_by("price").reverse()
    else:
        phones = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.filter(slug=slug)[0]
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
