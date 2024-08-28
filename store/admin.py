from django.contrib import admin

from store.models import Product

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("product_name", )}
    list_display = ("product_name", "price", "stock", "category", "created_date", "modified_date", "is_available")

admin.site.register(Product, ProductAdmin)
