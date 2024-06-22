from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'sinf', SinfViewSet)
router.register(r'davomat', DavomatViewSet)
router.register(r'vazifa', VazifaViewSet)
router.register(r'tolov', TolovViewSet)
router.register(r'yangilikvaelon', YangilikVaElonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    # path('success/', SuccessView.as_view(), name='success'),
    # path('cancel/', CancelView.as_view(), name='cancel'),
    # path('webhook/', StripeWebhookView.as_view(), name='stripe-webhook'),
]
