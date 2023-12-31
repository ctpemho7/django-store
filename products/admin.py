from django.contrib import admin

from products.models import Product, ProductCategory

# Register your models here. (отображение таблиц в админке)
admin.site.register(Product)
admin.site.register(ProductCategory)