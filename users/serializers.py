# serializers.py
from rest_framework import serializers
from .models import Oqituvchi, Oquvchi, Foydalanuvchi, OtaOna
from asosiy.serializers import SinfSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foydalanuvchi
        fields = ('id', 'username', 'email', 'roli')

class OtaOnaSerializers(serializers.ModelSerializer):
    class Meta:
        model = OtaOna
        fields = "__all__"

class OquvchiSerializers(serializers.ModelSerializer):
    sinfi = SinfSerializer()
    ota_ona = OtaOnaSerializers()
    foydalanuvchi = UserSerializer()
    class Meta:
        model = Oquvchi
        fields = "__all__"

class OqituvchiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Oqituvchi
        fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Foydalanuvchi
        fields = ('username', 'email', 'password', 'roli')

    def create(self, validated_data):
        user = Foydalanuvchi.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            roli=validated_data['roli']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)