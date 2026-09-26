from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.contrib.auth import authenticate, login

from .serializers import RegisterSerializer, LoginSerializer

class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'username': request.user.username,
            'email': request.user.email,
        })

class RegisterView(APIView):

    permission_classes = []

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {
                    'message': 'User registered successfully',
                    'username': user.username,
                    'email': user.email,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):

    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user is None:
                return Response(
                    {'detail': 'Invalid username or password.'},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            login(request, user)

            return Response({
                'message': 'Login successful.',
                'username': username,
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )