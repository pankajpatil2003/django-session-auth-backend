from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.middleware.csrf import get_token

from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer

# API View for user registration
class RegisterAPIView(APIView):
    permission_classes = [AllowAny] # Allow anyone to register

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Optionally log in the user immediately after registration
            login(request, user)
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API View for user login
class LoginAPIView(APIView):
    permission_classes = [AllowAny] # Allow anyone to attempt login

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user) # Establish the session
                # Get CSRF token for subsequent requests if frontend needs it
                csrf_token = get_token(request)
                return Response({
                    'message': 'Login successful',
                    'user': UserSerializer(user).data,
                    'csrf_token': csrf_token # Provide CSRF token for frontend
                }, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API View for user logout
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated] # Only authenticated users can logout

    def post(self, request):
        logout(request) # End the session
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)

# API View to check authentication status and get user details
class UserStatusAPIView(APIView):
    permission_classes = [IsAuthenticated] # Only authenticated users can access this

    def get(self, request):
        # If the request reaches here, the user is authenticated due to IsAuthenticated permission
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)

