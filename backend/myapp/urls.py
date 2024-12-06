from django.urls import path
from .views import (
    ContactAPIView,
    CreatePostAPIView,
    RetrievePostAPIView,
    UpdatePostAPIView,
    DeletePostAPIView,
    ProfileApi
)
from .view import home
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('contact/', ContactAPIView.as_view(), name='contact'),
    path('profile/', ProfileAPI.as_view(), name='profile'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('home/', name='home'),
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
