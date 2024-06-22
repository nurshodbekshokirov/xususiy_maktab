from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Sinf, Davomat, Vazifa, Tolov, YangilikVaElon
from .serializers import SinfSerializer, DavomatSerializer, VazifaSerializer, TolovSerializer, YangilikVaElonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Sinf ViewSet
class SinfViewSet(viewsets.ModelViewSet):
    queryset = Sinf.objects.all()
    serializer_class = SinfSerializer
    permission_classes = [IsAuthenticated]

# Davomat ViewSet
class DavomatViewSet(viewsets.ModelViewSet):
    queryset = Davomat.objects.all()
    serializer_class = DavomatSerializer
    permission_classes = [IsAuthenticated]

# Vazifa ViewSet
class VazifaViewSet(viewsets.ModelViewSet):
    queryset = Vazifa.objects.all()
    serializer_class = VazifaSerializer
    permission_classes = [IsAuthenticated]

# Tolov ViewSet
class TolovViewSet(viewsets.ModelViewSet):
    queryset = Tolov.objects.all()
    serializer_class = TolovSerializer
    permission_classes = [IsAuthenticated]

# YangilikVaElon ViewSet
class YangilikVaElonViewSet(viewsets.ModelViewSet):
    queryset = YangilikVaElon.objects.all()
    serializer_class = YangilikVaElonSerializer
    permission_classes = [IsAuthenticated]
#
# # Stripe To'lov view
# class CreateCheckoutSessionView(APIView):
#     def post(self, request, *args, **kwargs):
#         try:
#             # User va to'lov miqdorini olish
#             foydalanuvchi = request.user
#             miqdori = request.data.get('miqdori')
#
#             # Stripe sessiyasini yaratish
#             checkout_session = stripe.checkout.Session.create(
#                 payment_method_types=['card'],
#                 line_items=[
#                     {
#                         'price_data': {
#                             'currency': 'usd',
#                             'product_data': {
#                                 'name': 'To\'lov',
#                             },
#                             'unit_amount': int(float(miqdori) * 100),  # miqdorni sentlarda olish
#                         },
#                         'quantity': 1,
#                     },
#                 ],
#                 mode='payment',
#                 success_url=settings.STRIPE_SUCCESS_URL,
#                 cancel_url=settings.STRIPE_CANCEL_URL,
#             )
#
#             # To'lov modeliga stripe_payment_intent qo'shish
#             Tolov.objects.create(
#                 foydalanuvchi=foydalanuvchi,
#                 miqdori=miqdori,
#                 holati='pending',
#                 stripe_payment_intent=checkout_session.payment_intent
#             )
#
#             return Response({'id': checkout_session.id})
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
#
# # Muvaffaqiyatli to'lov view
# class SuccessView(APIView):
#     def get(self, request, *args, **kwargs):
#         return Response({"message": "To'lov muvaffaqiyatli amalga oshirildi"})
#
# # Bekor qilingan to'lov view
# class CancelView(APIView):
#     def get(self, request, *args, **kwargs):
#         return Response({"message": "To'lov bekor qilindi"})
#
# # Stripe webhook view
# @method_decorator(csrf_exempt, name='dispatch')
# class StripeWebhookView(APIView):
#     def post(self, request, *args, **kwargs):
#         payload = request.body
#         sig_header = request.META['HTTP_STRIPE_SIGNATURE']
#         event = None
#
#         try:
#             event = stripe.Webhook.construct_event(
#                 payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
#             )
#         except ValueError as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         except stripe.error.SignatureVerificationError as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
#         # Eventni qayta ishlash
#         if event['type'] == 'payment_intent.succeeded':
#             payment_intent = event['data']['object']
#             stripe_payment_intent = payment_intent['id']
#
#             # To'lov holatini yangilash
#             try:
#                 tolov = Tolov.objects.get(stripe_payment_intent=stripe_payment_intent)
#                 tolov.holati = 'paid'
#                 tolov.save()
#             except Tolov.DoesNotExist:
#                 pass
#
#         return Response(status=status.HTTP_200_OK)
