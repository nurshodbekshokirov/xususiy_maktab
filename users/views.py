
# views.py
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Oqituvchi, Oquvchi, Foydalanuvchi, OtaOna
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer, OquvchiSerializers, OqituvchiSerializers, OtaOnaSerializers
from rest_framework.viewsets import ModelViewSet

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"user": UserSerializer(user).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
            if user is not None:
                login(request, user)
                return Response({"user": UserSerializer(user).data}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

class OquvchiDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            oquvchi = Oquvchi.objects.get(id=pk)
            serializer = OquvchiSerializers(oquvchi)
            return Response(serializer.data)
        except Oquvchi.DoesNotExist:
            return Response({"error": "Oquvchi not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            oquvchi = Oquvchi.objects.get(id=pk)
            serializer = OquvchiSerializers(oquvchi, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Oquvchi.DoesNotExist:
            return Response({"error": "Oquvchi not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            oquvchi = Oquvchi.objects.get(id=pk)
            oquvchi.delete()
            return Response({"message": "Oquvchi deleted successfully"})
        except Oquvchi.DoesNotExist:
            return Response({"error": "Oquvchi not found"}, status=status.HTTP_404_NOT_FOUND)

class OquvchilarAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        oquvchilar = Oquvchi.objects.all()
        serializer = OquvchiSerializers(oquvchilar, many=True)
        return Response(serializer.data)

    def post(self, request):
        foydalanuvchi_id = request.data.get('foydalanuvchi')
        if not foydalanuvchi_id:
            return Response({'error': 'Foydalanuvchi ID kiritilmadi'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            foydalanuvchi = Foydalanuvchi.objects.get(id=foydalanuvchi_id)
        except Foydalanuvchi.DoesNotExist:
            return Response({'error': 'Bunday foydalanuvchi topilmadi'}, status=status.HTTP_404_NOT_FOUND)

        if Oquvchi.objects.filter(foydalanuvchi=foydalanuvchi).exists():
            return Response({'error': 'Bu foydalanuvchi uchun oquvchi allaqachon mavjud'}, status=status.HTTP_400_BAD_REQUEST)

        oquvchi_data = request.data.copy()
        oquvchi_data['foydalanuvchi'] = foydalanuvchi.id

        serializer = OquvchiSerializers(data=oquvchi_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OtaOnaAPIView(APIView):
    def get(self, request):
        ota_onalar = OtaOna.objects.all()
        serializer = OtaOnaSerializers(ota_onalar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OtaOnaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OtaOnaDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            ota_ona = OtaOna.objects.get(id=pk)
            serializer = OtaOnaSerializers(ota_ona)
            return Response(serializer.data)
        except OtaOna.DoesNotExist:
            return Response({"error": "OtaOna not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            ota_ona = OtaOna.objects.get(id=pk)
            ota_ona.delete()
            return Response({"message": "OtaOna deleted successfully"})
        except OtaOna.DoesNotExist:
            return Response({"error": "OtaOna not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            ota_ona = OtaOna.objects.get(id=pk)
            serializer = OtaOnaSerializers(ota_ona, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except OtaOna.DoesNotExist:
            return Response({"error": "OtaOna not found"}, status=status.HTTP_404_NOT_FOUND)

class OqituvchiMODELViewset(ModelViewSet):
    queryset = Oqituvchi.objects.all()
    serializer_class = OqituvchiSerializers