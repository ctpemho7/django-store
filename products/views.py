from django.shortcuts import render

from products.models import Product, ProductCategory


# Create your views here.
# функции = контроллеры = вьюхи
def index(request):
    return render(request, 'products/index.html')


def products(request):
    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context=context)
