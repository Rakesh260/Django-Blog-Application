import datetime

from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


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
            username = request.data.get('userName')
            password = request.data.get('password')
            user = User.objects.filter(username=username).first()

            if user and user.check_password(password):
                refresh = RefreshToken.for_user(user)
                response = Response()
                # response.set_cookie('access_token', str(refresh.access_token), max_age=3600, httponly=True)
                response.set_cookie(
                    'access_token',
                    str(refresh.access_token),
                    max_age=3600,
                    httponly=True,
                    secure=True,
                    samesite='None'
                )
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


class PostListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        user = request.user.id
        object_list = Post.objects.all().annotate(is_liked=Count('liked_by', filter=Q(liked_by__id=user))).order_by('-pk')
        number_of_items = request.query_params.get('pageLength')
        paginator = Paginator(object_list, number_of_items)
        objs = paginator.get_page(request.query_params.get('pageIndex'))
        serializer = PostSerializer(objs, many=True)
        return Response({'data': serializer.data, 'count': paginator.count})

    @staticmethod
    def post(request):
        try:
            data = dict(request.data)
            title = data.get('title').strip()
            content = data.get('content')
            user = request.user
            if Post.objects.filter(title=title).exists():
                return Response({'result': 'failure', 'msg': 'Title with same name exists'}, status=status.HTTP_400_BAD_REQUEST)
            Post.objects.create(title=title, content=content, author=user)
            return Response({'result': 'success', 'msg': 'Successfully created'}, status=status.HTTP_201_CREATED)
        except Exception as err:
            print(str(err))
            return Response(str(err), status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk):
        user = request.user
        serializer = Post.objects.filter(pk=pk).annotate(is_liked=Count('liked_by', filter=Q(liked_by=user))
                                                         )
        return Response({"data": PostSerializer(serializer).data, 'result': 'success'})

    def post(self, request, pk):
        post = self.get_object(pk)
        data = request.data
        title = data.get('title')
        content = data.get('content')
        liked_by = request.user.id
        if content:
            post.content = content
        if title:
            post.title = title
        if data.get('is_liked') == 'true':
            post.liked_by.add(liked_by)
        else:
            post.liked_by.remove(liked_by)
        post.save()
        serializer = PostSerializer(post, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = request.user.id
        post = self.get_object(pk)
        if post.author.id != user:
            return Response({"result": "failure", "error": "UnAuthorized Action"}, status=status.HTTP_200_OK)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        post_id = request.query_params.get('post_id')
        comments = Comment.objects.filter(post_id=post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        data = request.data
        data['post'] = data.get('post_id')
        data['author'] = request.user.id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get_object(pk):
        return get_object_or_404(Comment, pk=pk)

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def post(self, request, pk):
        user = request.user.id
        comment = self.get_object(pk)
        data = request.data
        if comment.author.id != user:
            return Response({"result": "failure", "error": "UnAuthorized Action"}, status=status.HTTP_200_OK)
        serializer = CommentSerializer(comment, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = request.user.id
        comment = self.get_object(pk)
        if comment.author.id != user:
            return Response({"result": "failure", "error": "UnAuthorized Action"}, status=status.HTTP_200_OK)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
