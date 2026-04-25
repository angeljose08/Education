from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VotingProcedureViewSet, VotingMethodViewSet

router = DefaultRouter()
router.register(r'procedures', VotingProcedureViewSet, basename='voting-procedure')
router.register(r'methods', VotingMethodViewSet, basename='voting-method')

urlpatterns = [
    path('', include(router.urls)),
]
