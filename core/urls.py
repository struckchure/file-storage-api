from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView

from core.api.authentication_api import LoginAPIView, RegistrationAPIView
from core.api.file_api import GetUpdateDeleteFileAPI, ListCreateFileAPI

app_name = "core"

file_urls = [
    path("files/", ListCreateFileAPI.as_view(), name="list-create-file"),
    path(
        "files/<slug:slug>/",
        GetUpdateDeleteFileAPI.as_view(),
        name="get-update-delete-file",
    ),
]

authnentication_urls = [
    path("auth/register/", RegistrationAPIView.as_view(), name="register_view"),
    path("auth/login/", LoginAPIView.as_view(), name="login_view"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
]

urlpatterns = [
    *file_urls,
    *authnentication_urls,
]
