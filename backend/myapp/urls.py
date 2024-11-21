from django.urls import path
from .views import Postview, ContactAPIView

urlpatterns = [
    path('post/', Postview.as_view({'get': 'list', 'post': 'create'}), name='post_list_create'),
    path('post/<int:pk>/', Postview.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post_detail'),
    path("contact/", ContactAPIView.as_view(), name='contact'),
]

# Static and media URL configuration for development purposes
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
