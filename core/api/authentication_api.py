from core.serializers.authentication_serializers import (
    LoginSerializer,
    RegistrationSerializer,
)
from file_storage.decorators import handle_errors
from file_storage.utils import get_tokens_for_user
from rest_framework import generics, status
from rest_framework.response import Response


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    @handle_errors()
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokens = get_tokens_for_user(serializer.instance)

        return Response(
            {"data": {**serializer.data, **tokens}},
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    @handle_errors()
    def post(self, request):
        login_serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        login_serializer.is_valid(raise_exception=True)
        login_serializer.save()

        tokens = get_tokens_for_user(login_serializer.instance)

        return Response(
            {"data": {**login_serializer.data, **tokens}}, status=status.HTTP_200_OK
        )
