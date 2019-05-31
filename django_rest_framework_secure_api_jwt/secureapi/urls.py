from django.contrib import admin
from django.urls import path
from secureapi.api.views import AuthenticatedView, AdminView
from health.views import health

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authenticated/', AuthenticatedView.as_view(), name='authenticated'),
    path('adminview/', AdminView.as_view(), name='authenticated'),
    path('health/', health),
]
