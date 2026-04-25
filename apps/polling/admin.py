from django.contrib import admin
from .models import PollingLocation, PollingDistrict, EarlyVotingLocation

@admin.register(PollingLocation)
class PollingLocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state', 'election_year', 'is_active']
    list_filter = ['state', 'election_year', 'is_active']
    search_fields = ['name', 'address', 'city']
    ordering = ['state', 'city', 'name']


@admin.register(PollingDistrict)
class PollingDistrictAdmin(admin.ModelAdmin):
    list_display = ['district_id', 'name', 'state', 'election_year']
    list_filter = ['state', 'election_year']
    search_fields = ['district_id', 'name']
    filter_horizontal = ['polling_locations']


@admin.register(EarlyVotingLocation)
class EarlyVotingLocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state', 'election_year', 'start_date', 'end_date', 'is_active']
    list_filter = ['state', 'election_year', 'is_active']
    search_fields = ['name', 'address', 'city']
    ordering = ['-start_date', 'state']
