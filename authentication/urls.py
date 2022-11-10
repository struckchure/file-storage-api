from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView

from authentication.api import LoginAPIView, RegistrationAPIView

urlpatterns = [
    path("auth/register/", RegistrationAPIView.as_view(), name="register_view"),
    path("auth/login/", LoginAPIView.as_view(), name="login_view"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
]
