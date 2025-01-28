from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from .serializers import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


@api_view(["POST"])
def user_register(request):
    if request.method == "POST":
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["email"] = account.email
            data["response"] = "account has been created"

            refresh = RefreshToken.for_user(account)

            data["token"] = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        else:
            data = serializer.errors

        return Response(data, status=status.HTTP_200_OK)


@api_view(["POST"])
def logout_user(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response({"message": "your are logged out "},status=status.HTTP_200_OK)


@api_view(["POST"])
def login_user(request):
    dicti = {}
    if request.method == "POST":
        data = TokenObtainPairSerializer(data=request.data)
        if data.is_valid():
            dicti = {
                "access": data.validated_data["access"],
                "refresh": data.validated_data["refresh"],
            }

    return Response(dicti, status=status.HTTP_200_OK)
