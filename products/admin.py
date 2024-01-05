from django.contrib import admin

from products.models import Product, ProductCategory, Basket

# Register your models here. (отображение таблиц в админке)
# admin.site.register(Product)
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name', '-price', 'quantity')

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')