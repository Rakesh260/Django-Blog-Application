from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import Post
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            print(err)
            return Response({'err': str(err)})


class LoginView(APIView):

    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = User.objects.filter(username=username).first()

            if user and user.check_password(password):
                refresh = RefreshToken.for_user(user)
                response = Response()
                response.set_cookie('access_token', str(refresh.access_token), max_age=3600, httponly=True)
                response.data = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }
                return response
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            print(err)
            return Response({'err': str(err)})


class GetUserDataView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class GetPosts(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        try:
            filters = request.query_params
            post_data = Post.objects.filter()
            return Response({'data': post_data},  status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({'err': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        response = Response()
        response.delete_cookie('access_token')
        return response
