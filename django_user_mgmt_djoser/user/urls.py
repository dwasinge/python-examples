from django.urls import path
from rest_framework_simplejwt import views
from . import views as custom_views

urlpatterns = [
    path('jwt/create/', custom_views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', views.TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', views.TokenVerifyView.as_view(), name='jwt-verify'),
]

