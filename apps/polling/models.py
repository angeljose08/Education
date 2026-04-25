from django.db import models
from django.contrib.gis.db import models as gis_models
from apps.core.models import TimeStampedModel

class PollingLocation(TimeStampedModel):
    """Model for polling locations."""
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    election_year = models.IntegerField()
    hours_open = models.TimeField(blank=True, null=True)
    hours_close = models.TimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    accessibility_features = models.JSONField(default=list, blank=True, help_text="List of accessibility features")

    class Meta:
        ordering = ['state', 'city', 'name']
        indexes = [
            models.Index(fields=['state', 'election_year']),
            models.Index(fields=['city', 'state']),
        ]

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"


class PollingDistrict(TimeStampedModel):
    """Model for polling districts/precincts."""
    district_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=100, blank=True)
    election_year = models.IntegerField()
    polling_locations = models.ManyToManyField(PollingLocation, related_name='districts')

    class Meta:
        ordering = ['state', 'district_id']
        unique_together = [['district_id', 'state', 'election_year']]

    def __str__(self):
        return f"{self.district_id} - {self.state}"


class EarlyVotingLocation(TimeStampedModel):
    """Model for early voting locations."""
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    election_year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    hours_open = models.TimeField(blank=True, null=True)
    hours_close = models.TimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['state', 'start_date']

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"
