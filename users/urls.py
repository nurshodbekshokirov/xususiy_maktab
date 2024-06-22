from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("oqituvchi",OqituvchiMODELViewset)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('oquvchi/<int:pk>/', OquvchiDetailsAPIView.as_view(), name='oquvchi_details'),

    path("oquvchilar/", OquvchilarAPIView.as_view(), name="oquvchilar"),
    path("ota_onalar/", OtaOnaAPIView.as_view(), name="ota_onalar"),
    path("ota_onalar/<int:pk>/", OtaOnaDetailAPIView.as_view(),name="ota_onalar_details"),
    path("", include(router.urls)),
]
