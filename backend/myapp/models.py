from django.db import models
from django.contrib.auth.models import User  # Corrected import for the User model

class Post(models.Model):
    title = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Corrected field name and added `User`
    image = models.ImageField(upload_to="images/profile")  # Removed the leading slash in `upload_to`
    age = models.IntegerField(default=0)  # Corrected `Intergerfile` to `IntegerField` and `Default` to `default`
    is_verified = models.BooleanField(default=False)  # Changed `isVerified` to `is_verified` for naming convention
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

