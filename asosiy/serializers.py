from rest_framework import serializers
from .models import Sinf, Davomat, Vazifa, Tolov, YangilikVaElon
from users.models import *

class SinfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sinf
        fields = ['id', 'nomi', 'oqituvchi']

class DavomatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = ['id', 'oquvchi', 'sana', 'holati']

class VazifaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vazifa
        fields = ['id', 'sinfi', 'mavzu', 'tavsif', 'muddati']

class TolovSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tolov
        fields = ['id', 'foydalanuvchi', 'miqdori', 'sana', 'holati']

class YangilikVaElonSerializer(serializers.ModelSerializer):
    class Meta:
        model = YangilikVaElon
        fields = ['id', 'mavzu', 'matn', 'yaratilgan_vaqt', 'yangilangan_vaqt']
