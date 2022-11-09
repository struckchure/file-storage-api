from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from authentication.serializers import MyTokenObtainPairSerializer, RegistrationSerializer
from authentication.utils import get_tokens_for_user
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics, status


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            username = serializer.data['username']
            user = User.objects.get(username=username)
            tokens = get_tokens_for_user(user)
            return Response({"user": serializer.data, "auth": tokens}, status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


registration_view = RegistrationAPIView.as_view()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

login_view = MyTokenObtainPairView.as_view()