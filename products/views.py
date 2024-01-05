from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from products.models import Product, ProductCategory, Basket


# Create your views here.
# функции = контроллеры = вьюхи
def index(request):
    return render(request, 'products/index.html')


def products(request, category_id=None):

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    context = {
        'products': products,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context=context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        item = basket.last()
        item.quantity += 1
        item.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    item = Basket.objects.get(id=basket_id)
    item.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
