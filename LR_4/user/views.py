from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer

class RegistrView(APIView):

    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if serializer.is_valid(raise_exception = True):
            serializer.save()

            return Response({
                "status": "succes"
            }, 200)

        return Response ({
            "status": "error",
        })

class Logout(APIView):

    permission_classes = [AllowAny, ]

    def post(self, request):
        try:
            refresh = request.data.get('refresh')
            token = RefreshToken(refresh)
            token.blacklist()
        except Exception as e:
            return Response ({
                "error": "Wrong Refresh Token!",
            }, 400)

        return Response ({
            "status": "Logged out",
        }, 200)

class Auth(APIView):

    permission_classes = [AllowAny, ]

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        try:
            token = RefreshToken.for_user(user)
        except Exception as e:
            return Response({"error": "Неверный логин или пароль!"}, status=400)

        return Response({"refresh": str(token),
                         "access": str(token.access_token),
                        }, status=200)

class TakeToken(APIView):

    def get(self, request):
        return Response({
            "status": "success",
        })
