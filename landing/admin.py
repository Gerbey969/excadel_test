from django.contrib import admin
from .models import *

class RestaurantAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Restaurant._meta.fields]

    class Meta:
        model = Restaurant

admin.site.register(Restaurant, RestaurantAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Products._meta.fields]

    class Meta:
        model = Restaurant

admin.site.register(Products, ProductsAdmin)