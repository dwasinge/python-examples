from django.urls import path, include
from health.views import health

urlpatterns = [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('health/', health),
]
