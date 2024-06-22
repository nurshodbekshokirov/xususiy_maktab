from django.contrib import admin
from .models import *


admin.site.register(Oqituvchi)
admin.site.register(Oquvchi)
admin.site.register(OtaOna)
admin.site.register(Foydalanuvchi)
for model in [Foydalanuvchi, Oqituvchi, Oquvchi, OtaOna]:
    if admin.site.is_registered(model):
        admin.site.unregister(model)



@admin.register(Foydalanuvchi)
class FoydalanuvchiAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'roli')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('roli',)

@admin.register(Oqituvchi)
class OqituvchiAdmin(admin.ModelAdmin):
    list_display = ('foydalanuvchi', 'ismi', 'fan', 'telefon_raqami', 'email')
    search_fields = ('foydalanuvchi__username', 'ismi', 'fan', 'email')
    list_filter = ('fan',)

@admin.register(Oquvchi)
class OquvchiAdmin(admin.ModelAdmin):
    list_display = ('foydalanuvchi', 'ismi', 'sinfi', 'tugilgan_sanasi', 'ota_ona')
    search_fields = ('foydalanuvchi__username', 'ismi', 'sinfi__name', 'ota_ona__ismi')
    list_filter = ('sinfi', 'tugilgan_sanasi')

@admin.register(OtaOna)
class OtaOnaAdmin(admin.ModelAdmin):
    list_display = ('foydalanuvchi', 'ismi', 'tugilgan_sana', 'telefon_raqami', 'email')
    search_fields = ('foydalanuvchi__username', 'ismi', 'email')
    list_filter = ('tugilgan_sana',)

# Register your models here.


# Register your models here.
