from django.urls import path, include
from health.views import health

urlpatterns = [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('user.urls')),
    path('health/', health),
]
