from django.db import models
from apps.core.models import TimeStampedModel

class VotingProcedure(TimeStampedModel):
    """Model for voting procedures and guidelines."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    state = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(
        max_length=50,
        choices=[
            ('registration', 'Registration'),
            ('voting_methods', 'Voting Methods'),
            ('day_of_voting', 'Day of Voting'),
            ('accessibility', 'Accessibility'),
            ('requirements', 'Requirements'),
        ]
    )
    content = models.TextField()
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Voting Procedure'
        verbose_name_plural = 'Voting Procedures'

    def __str__(self):
        return self.title


class VotingMethod(TimeStampedModel):
    """Model for different voting methods."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    pros = models.JSONField(default=list)
    cons = models.JSONField(default=list)
    availability_states = models.JSONField(default=list, help_text="List of states where this method is available")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
