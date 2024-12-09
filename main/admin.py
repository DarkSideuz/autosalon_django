from django.contrib import admin

# Register your models here.

from .models import Brand, Car

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand')
