from django.db import models
from django.contrib.auth import User

class Post(models.Model):
    title = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=225)
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
class Profile(models.Model):
    User = models.ForeignKey(ondelete = models.CASCADE)
    age = models.Intergerfile(Default = 0)
    isVerified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.User.username
    