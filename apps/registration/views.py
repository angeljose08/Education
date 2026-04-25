from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import RegistrationRequirement, RegistrationMethod, RegistrationDeadline
from .serializers import (
    RegistrationRequirementSerializer,
    RegistrationMethodSerializer,
    RegistrationDeadlineSerializer
)


class RegistrationRequirementViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for voter registration requirements."""
    queryset = RegistrationRequirement.objects.all()
    serializer_class = RegistrationRequirementSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['state', 'requirement', 'description']

    @action(detail=False, methods=['get'])
    def by_state(self, request):
        state = request.query_params.get('state')
        if state:
            requirements = self.queryset.filter(state=state.upper())
            serializer = self.get_serializer(requirements, many=True)
            return Response(serializer.data)
        return Response({'error': 'State parameter required'}, status=400)


class RegistrationMethodViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for voter registration methods."""
    queryset = RegistrationMethod.objects.all()
    serializer_class = RegistrationMethodSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['state', 'method', 'description']

    @action(detail=False, methods=['get'])
    def by_state(self, request):
        state = request.query_params.get('state')
        if state:
            methods = self.queryset.filter(state=state.upper())
            serializer = self.get_serializer(methods, many=True)
            return Response(serializer.data)
        return Response({'error': 'State parameter required'}, status=400)


class RegistrationDeadlineViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for voter registration deadlines."""
    queryset = RegistrationDeadline.objects.all()
    serializer_class = RegistrationDeadlineSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['state']

    @action(detail=False, methods=['get'])
    def by_state(self, request):
        state = request.query_params.get('state')
        if state:
            deadlines = self.queryset.filter(state=state.upper())
            serializer = self.get_serializer(deadlines, many=True)
            return Response(serializer.data)
        return Response({'error': 'State parameter required'}, status=400)
