from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Postview
from .views import ContactAPIView

urlpatterns = [
    path('', Postview.as_view(), name='post_list'),
    path('/<int:pk>', Postview.as_view(), name='post_detail'),
    path("/contact" ,ContactAPIView.as_view(),name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)