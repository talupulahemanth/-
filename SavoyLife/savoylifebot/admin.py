from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('dish_name', 'dish_type', 'allergens')
    list_filter = ('dish_type',)
    search_fields = ('dish_name', 'allergens')
