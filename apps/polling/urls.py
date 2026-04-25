from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PollingLocationViewSet, PollingDistrictViewSet, EarlyVotingLocationViewSet

router = DefaultRouter()
router.register(r'locations', PollingLocationViewSet, basename='polling-location')
router.register(r'districts', PollingDistrictViewSet, basename='polling-district')
router.register(r'early-voting', EarlyVotingLocationViewSet, basename='early-voting-location')

urlpatterns = [
    path('', include(router.urls)),
]
