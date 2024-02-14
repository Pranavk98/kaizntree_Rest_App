from django.urls import path, include
from django.urls import path, re_path
from django.conf.urls import url



from rest_framework.routers import DefaultRouter
from .views import ItemViewSet  # Import your viewsets here

router = DefaultRouter()
router.register(r'items', ItemViewSet)  # Example route for ItemViewSet

urlpatterns = [
    path('', include(router.urls)),
]
