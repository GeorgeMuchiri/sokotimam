from django.contrib import admin

from .models import Products, Store, Category, Subcategory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'slug']
    prepopulated_fields = { 'slug': ('name', )}




@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'owner', 'slug']
    prepopulated_fields = {'slug':('name',)}
    

@admin.register(Subcategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'Category']

# admin.site.register(Store)
# admin.site.register(Products)
