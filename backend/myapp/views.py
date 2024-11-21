from rest_framework import response, permissions, status, viewsets
from rest_framework.views import APIView  # Correct import for APIView
from rest_framework.response import Response  # Correct import for Response
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer, ContactSerilizer


# Contact View
class ContactAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the contact message to the database
            # You can optionally send an email here using the contact details.
            return Response({"message": "Contact message submitted successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Post View using ViewSets
class Postview(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)  # Corrected reference to 'Post' model
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)  # Corrected reference to 'Post' model
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)  # Corrected reference to 'Post' model
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

