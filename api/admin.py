from django.contrib import admin
from .models import Product, Category, Profile


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', "price", "is_available", "discount")

    search_fields = ("name", "category",)
    list_editable = ['price', 'is_available', "discount"]
    prepopulated_fields = {'slug': ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {'slug': ("name",)}


admin.site.register(Profile)
