from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import PollingLocation, PollingDistrict, EarlyVotingLocation
from .serializers import (
    PollingLocationSerializer,
    PollingDistrictSerializer,
    EarlyVotingLocationSerializer
)


class PollingLocationViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for polling locations with filtering by location and election year."""
    queryset = PollingLocation.objects.filter(is_active=True)
    serializer_class = PollingLocationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'city', 'address']

    @action(detail=False, methods=['get'])
    def by_state(self, request):
        state = request.query_params.get('state')
        if state:
            locations = self.queryset.filter(state=state.upper())
            serializer = self.get_serializer(locations, many=True)
            return Response(serializer.data)
        return Response({'error': 'State parameter required'}, status=400)

    @action(detail=False, methods=['get'])
    def by_city(self, request):
        city = request.query_params.get('city')
        state = request.query_params.get('state')
        if city and state:
            locations = self.queryset.filter(city__icontains=city, state=state.upper())
            serializer = self.get_serializer(locations, many=True)
            return Response(serializer.data)
        return Response({'error': 'City and state parameters required'}, status=400)

    @action(detail=False, methods=['get'])
    def nearby(self, request):
        """Find polling locations near a given latitude and longitude."""
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')
        radius = request.query_params.get('radius', 5)  # Default 5 miles
        
        if lat and lon:
            try:
                lat = float(lat)
                lon = float(lon)
                radius = float(radius)
                # Simplified distance calculation (approximately 1 degree = 69 miles)
                locations = self.queryset.filter(
                    latitude__gte=lat - radius/69,
                    latitude__lte=lat + radius/69,
                    longitude__gte=lon - radius/69,
                    longitude__lte=lon + radius/69,
                )
                serializer = self.get_serializer(locations, many=True)
                return Response(serializer.data)
            except ValueError:
                return Response({'error': 'Invalid latitude or longitude'}, status=400)
        return Response({'error': 'Latitude and longitude parameters required'}, status=400)


class PollingDistrictViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for polling districts."""
    queryset = PollingDistrict.objects.all()
    serializer_class = PollingDistrictSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['district_id', 'name', 'state']

    @action(detail=False, methods=['get'])
    def by_state(self, request):
        state = request.query_params.get('state')
        if state:
            districts = self.queryset.filter(state=state.upper())
            serializer = self.get_serializer(districts, many=True)
            return Response(serializer.data)
        return Response({'error': 'State parameter required'}, status=400)


class EarlyVotingLocationViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for early voting locations."""
    queryset = EarlyVotingLocation.objects.filter(is_active=True)
    serializer_class = EarlyVotingLocationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'city', 'state']

    @action(detail=False, methods=['get'])
    def by_state(self, request):
        state = request.query_params.get('state')
        if state:
            locations = self.queryset.filter(state=state.upper())
            serializer = self.get_serializer(locations, many=True)
            return Response(serializer.data)
        return Response({'error': 'State parameter required'}, status=400)
