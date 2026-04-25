from django.db import models
from apps.core.models import TimeStampedModel

class RegistrationRequirement(TimeStampedModel):
    """Model for voter registration requirements."""
    state = models.CharField(max_length=2)
    requirement = models.CharField(
        max_length=100,
        choices=[
            ('age', 'Age'),
            ('citizenship', 'Citizenship'),
            ('residency', 'Residency'),
            ('identification', 'Identification'),
            ('other', 'Other'),
        ]
    )
    description = models.TextField()
    details = models.TextField(blank=True)
    deadline_days_before = models.IntegerField(null=True, blank=True, help_text="Days before election")

    class Meta:
        ordering = ['state', 'requirement']
        verbose_name = 'Registration Requirement'

    def __str__(self):
        return f"{self.state} - {self.requirement}"


class RegistrationMethod(TimeStampedModel):
    """Model for voter registration methods."""
    state = models.CharField(max_length=2)
    method = models.CharField(
        max_length=100,
        choices=[
            ('online', 'Online'),
            ('mail', 'Mail'),
            ('in_person', 'In Person'),
            ('driver_license', 'Driver License Office'),
            ('automatic', 'Automatic Registration'),
        ]
    )
    description = models.TextField()
    website_url = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    location_info = models.TextField(blank=True)

    class Meta:
        ordering = ['state', 'method']
        indexes = [
            models.Index(fields=['state', 'method']),
        ]

    def __str__(self):
        return f"{self.state} - {self.method}"


class RegistrationDeadline(TimeStampedModel):
    """Model for registration deadlines by state."""
    state = models.CharField(max_length=2)
    election_year = models.IntegerField()
    registration_deadline = models.DateField()
    election_date = models.DateField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-election_year', 'state']
        unique_together = [['state', 'election_year']]

    def __str__(self):
        return f"{self.state} - {self.election_year}"
