from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidateViewSet, CandidateComparisonViewSet

router = DefaultRouter()
router.register(r'', CandidateViewSet, basename='candidate')
router.register(r'comparisons', CandidateComparisonViewSet, basename='candidate-comparison')

urlpatterns = [
    path('', include(router.urls)),
]
