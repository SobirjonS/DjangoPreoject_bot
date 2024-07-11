# views.py
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    UserSerializer,
    LoginSerializer
    )
from .schemas import (
    register_response_schema,
    login_response_schema,
    user_schema,
    )

User = get_user_model()

class BaseTokenView(APIView):
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class RegisterAPIView(BaseTokenView):
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            201: openapi.Response(
                description="Successful registration",
                schema=register_response_schema
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING)
                })
            )
        },
        operation_description="Register a new user"
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            tokens = self.get_tokens_for_user(user)
            return Response({
                'user': serializer.data,
                **tokens
            }, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(BaseTokenView):
    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            200: openapi.Response(
                description="Successful login",
                schema=login_response_schema
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING)
                })
            ),
            401: openapi.Response(
                description="Authentication Failed",
                schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING)
                })
            )
        },
        operation_description="Login user"
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise AuthenticationFailed("User not found.")

            if not user.check_password(password):
                raise AuthenticationFailed("Incorrect password.")

            tokens = self.get_tokens_for_user(user)
            return Response(tokens, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class UpdateUserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            200: openapi.Response(
                description="Successful update",
                schema=user_schema()
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING)
                })
            )
        },
        operation_description="Update user information"
    )
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
            
            
class DeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)