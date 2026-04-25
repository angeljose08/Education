from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegistrationRequirementViewSet,
    RegistrationMethodViewSet,
    RegistrationDeadlineViewSet
)

router = DefaultRouter()
router.register(r'requirements', RegistrationRequirementViewSet, basename='registration-requirement')
router.register(r'methods', RegistrationMethodViewSet, basename='registration-method')
router.register(r'deadlines', RegistrationDeadlineViewSet, basename='registration-deadline')

urlpatterns = [
    path('', include(router.urls)),
]
