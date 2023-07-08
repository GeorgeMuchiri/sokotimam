from django.contrib import admin

from .models import Inventory, Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'inventory')


admin.site.register(Shop, ShopAdmin)
admin.site.register(Inventory)
