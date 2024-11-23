from django.urls import path
from .views import (
    ContactAPIView,
    CreatePostAPIView,
    RetrievePostAPIView,
    UpdatePostAPIView,
    DeletePostAPIView,
)

urlpatterns = [
    path('contact/', ContactAPIView.as_view(), name='contact'),
    path('posts/create/', CreatePostAPIView.as_view(), name='create_post'),
    path('posts/<int:pk>/', RetrievePostAPIView.as_view(), name='retrieve_post'),
    path('posts/<int:pk>/update/', UpdatePostAPIView.as_view(), name='update_post'),
    path('posts/<int:pk>/delete/', DeletePostAPIView.as_view(), name='delete_post'),
]


# Static and media URL configuration for development purposes
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
