from django.contrib import admin
from .models import *
# admin.site.register(Sinf)
# admin.site.register(Tolov)
# admin.site.register(Davomat)
# admin.site.register(Vazifa)
# admin.site.register(YangilikVaElon)

@admin.register(Sinf)
class SinfAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'oqituvchi')
    search_fields = ('nomi', 'oqituvchi__username')
    list_filter = ('nomi',)

@admin.register(Davomat)
class DavomatAdmin(admin.ModelAdmin):
    list_display = ('oquvchi', 'sana', 'holati')
    search_fields = ('oquvchi__ismi', 'sana', 'holati')
    list_filter = ('holati', 'sana')

@admin.register(Vazifa)
class VazifaAdmin(admin.ModelAdmin):
    list_display = ('sinfi', 'mavzu', 'muddati')
    search_fields = ('sinfi__nomi', 'mavzu')
    list_filter = ('muddati', 'sinfi')

@admin.register(Tolov)
class TolovAdmin(admin.ModelAdmin):
    list_display = ('foydalanuvchi', 'miqdori', 'sana', 'holati')
    search_fields = ('foydalanuvchi__username', 'miqdori', 'sana', 'holati')
    list_filter = ('holati', 'sana')

@admin.register(YangilikVaElon)
class YangilikVaElonAdmin(admin.ModelAdmin):
    list_display = ('mavzu', 'yaratilgan_vaqt', 'yangilangan_vaqt')
    search_fields = ('mavzu',)
    list_filter = ('yaratilgan_vaqt', 'yangilangan_vaqt')
# Register your models here.
