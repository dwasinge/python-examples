from django.urls import path, include
from health.views import health

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('health/', health),
]
