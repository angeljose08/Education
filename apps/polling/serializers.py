from rest_framework import serializers
from .models import PollingLocation, PollingDistrict, EarlyVotingLocation

class PollingLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollingLocation
        fields = ['id', 'name', 'address', 'city', 'state', 'zip_code', 'phone', 'website',
                  'latitude', 'longitude', 'election_year', 'hours_open', 'hours_close',
                  'accessibility_features', 'created_at']
        read_only_fields = ['id', 'created_at']


class PollingDistrictSerializer(serializers.ModelSerializer):
    polling_locations = PollingLocationSerializer(many=True, read_only=True)

    class Meta:
        model = PollingDistrict
        fields = ['id', 'district_id', 'name', 'state', 'county', 'election_year', 'polling_locations', 'created_at']
        read_only_fields = ['id', 'created_at']


class EarlyVotingLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EarlyVotingLocation
        fields = ['id', 'name', 'address', 'city', 'state', 'zip_code', 'phone', 'latitude',
                  'longitude', 'election_year', 'start_date', 'end_date', 'hours_open',
                  'hours_close', 'created_at']
        read_only_fields = ['id', 'created_at']
