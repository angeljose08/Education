from django.db import models
from apps.core.models import TimeStampedModel

class Candidate(TimeStampedModel):
    """Model for election candidates."""
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    party = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField()
    image = models.ImageField(upload_to='candidates/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    office_sought = models.CharField(max_length=255)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    election_year = models.IntegerField()
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['position', 'election_year']),
            models.Index(fields=['state', 'position']),
        ]

    def __str__(self):
        return f"{self.name} - {self.position}"


class CandidatePolicy(TimeStampedModel):
    """Model for candidate policies and positions."""
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='policies')
    issue = models.CharField(max_length=100)
    position = models.TextField()
    source_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Candidate Policies'
        indexes = [
            models.Index(fields=['candidate', 'issue']),
        ]

    def __str__(self):
        return f"{self.candidate.name} - {self.issue}"


class CandidateComparison(TimeStampedModel):
    """Model to store candidate comparisons."""
    candidates = models.ManyToManyField(Candidate)
    position = models.CharField(max_length=100)
    election_year = models.IntegerField()
    created_by_user = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comparison for {self.position} - {self.election_year}"
