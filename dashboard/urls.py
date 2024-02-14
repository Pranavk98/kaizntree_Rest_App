from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet  # Import your viewsets here

router = DefaultRouter()
router.register(r'items', ItemViewSet)  # Example route for ItemViewSet

urlpatterns = [
    path('', include(router.urls)),
]
