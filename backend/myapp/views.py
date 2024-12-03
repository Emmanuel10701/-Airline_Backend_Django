from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer, ContactSerilizer
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return JsonResponse({'message': 'Login successful'}, status=200)
    return JsonResponse({'error': 'Invalid credentials'}, status=400)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'}, status=200)


# Contact View
class ContactAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ContactSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response({"message": "Contact message submitted successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create Post View
class CreatePostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve Single Post View
class RetrievePostAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


# Update Post View
class UpdatePostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete Post View
class DeletePostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response({"message": "Post deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
