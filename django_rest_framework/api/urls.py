from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('people', views.PersonViewSet, base_name="people")
urlpatterns = router.urls
