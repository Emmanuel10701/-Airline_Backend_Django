from django.urls import path,include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
    ]