from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import VotingProcedure, VotingMethod
from .serializers import VotingProcedureSerializer, VotingMethodSerializer


class VotingProcedureViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing voting procedures."""
    queryset = VotingProcedure.objects.filter(is_published=True)
    serializer_class = VotingProcedureSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'category']

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category = request.query_params.get('category')
        if category:
            procedures = self.queryset.filter(category=category)
            serializer = self.get_serializer(procedures, many=True)
            return Response(serializer.data)
        return Response({'error': 'Category parameter required'}, status=400)

    @action(detail=False, methods=['get'])
    def by_state(self, request):
        state = request.query_params.get('state')
        if state:
            procedures = self.queryset.filter(state=state)
            serializer = self.get_serializer(procedures, many=True)
            return Response(serializer.data)
        return Response({'error': 'State parameter required'}, status=400)


class VotingMethodViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing voting methods."""
    queryset = VotingMethod.objects.all()
    serializer_class = VotingMethodSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
