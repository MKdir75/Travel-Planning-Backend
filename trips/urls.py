from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripViewSet, HotelViewSet, TransportViewSet

router = DefaultRouter()
router.register(r'trips', TripViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'transports', TransportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
