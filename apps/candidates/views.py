from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Candidate, CandidateComparison
from .serializers import CandidateSerializer, CandidateComparisonSerializer


class CandidateViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing candidates."""
    queryset = Candidate.objects.filter(is_published=True)
    serializer_class = CandidateSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'position', 'office_sought', 'party']
    ordering_fields = ['name', 'position']

    @action(detail=False, methods=['get'])
    def by_position(self, request):
        position = request.query_params.get('position')
        if position:
            candidates = self.queryset.filter(position=position)
            serializer = self.get_serializer(candidates, many=True)
            return Response(serializer.data)
        return Response({'error': 'Position parameter required'}, status=400)

    @action(detail=False, methods=['get'])
    def by_state(self, request):
        state = request.query_params.get('state')
        if state:
            candidates = self.queryset.filter(state=state)
            serializer = self.get_serializer(candidates, many=True)
            return Response(serializer.data)
        return Response({'error': 'State parameter required'}, status=400)

    @action(detail=False, methods=['get'])
    def by_year(self, request):
        year = request.query_params.get('year')
        if year:
            candidates = self.queryset.filter(election_year=year)
            serializer = self.get_serializer(candidates, many=True)
            return Response(serializer.data)
        return Response({'error': 'Year parameter required'}, status=400)


class CandidateComparisonViewSet(viewsets.ModelViewSet):
    """ViewSet for creating and viewing candidate comparisons."""
    queryset = CandidateComparison.objects.all()
    serializer_class = CandidateComparisonSerializer

    def perform_create(self, serializer):
        serializer.save(created_by_user=True)
