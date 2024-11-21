from rest_framework import responce
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import status
from .models import post
from .serializers import PostSerializers

class Post(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.AllowAny]


    def create(self,args,kwargs):
        serializer = self.serializer_class(data=args.data)
        if serializer.is_valid():
            serializer.save()
            return responce.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return responce.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

