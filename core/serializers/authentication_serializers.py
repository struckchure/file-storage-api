from django.contrib.auth import authenticate, get_user_model, login
from file_storage import exceptions
from rest_framework import serializers, status

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255, min_length=1, required=False)
    last_name = serializers.CharField(max_length=255, min_length=1, required=False)
    email = serializers.EmailField(max_length=255, min_length=6, required=False)
    password = serializers.CharField(max_length=100, min_length=4, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    def create(self, validated_data):
        user = authenticate(**validated_data)
        if not user:
            raise exceptions.Exception(
                "Invalid credentials", code=status.HTTP_401_UNAUTHORIZED
            )

        if self.context.get("request"):
            login(self.context["request"], user)

        return user
