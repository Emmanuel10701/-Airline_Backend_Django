from rest_framework import responce
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import status
from .models import post
from .serializers import PostSerializers
from django.shortcuts import  get_object_or_404


class Postview(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.AllowAny]


    def create(self,args,kwargs):
        serializer = self.serializer_class(data=args.data)
        if serializer.is_valid():
            serializer.save()
            return responce.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return responce.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, pk=None):
        post = get_object_or_404(post, pk=pk)
        serializer = PostSerializers(post)
        return responce.Response(serializer.data)
    
    def update(self, request, pk=None):
        post = get_object_or_404(post, pk=pk)
        serializer = PostSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return responce.Response(serializer.data)
        return responce.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        post = get_object_or_404(post, pk=pk)
        post.delete()
        return responce.Response(status=status.HTTP_204_NO_CONTENT)
    
