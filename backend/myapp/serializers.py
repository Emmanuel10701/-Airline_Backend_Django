from rest_framework import serializers
from .models import Post  
from .models import Contact
from .models import Profile

class ContactSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = "__all__"
        

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields = "__all__"