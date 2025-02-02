# places/admin.py

from django.contrib import admin
from .models import Place, PlaceImage, PlaceAddress, Category


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1  # Количество дополнительных форм для добавления

class PlaceAddressInline(admin.TabularInline):
    model = PlaceAddress
    extra = 1  # Количество дополнительных форм для добавления

class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline, PlaceAddressInline]  # Включите изображения и адреса в админке

# Регистрация моделей
admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage)  # Можно зарегистрировать отдельно, если нужно
admin.site.register(PlaceAddress)  # Можно зарегистрировать отдельно, если нужно
admin.site.register(Category)
