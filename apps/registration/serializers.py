from rest_framework import serializers
from .models import RegistrationRequirement, RegistrationMethod, RegistrationDeadline

class RegistrationRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationRequirement
        fields = ['id', 'state', 'requirement', 'description', 'details', 'deadline_days_before']
        read_only_fields = ['id']


class RegistrationMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationMethod
        fields = ['id', 'state', 'method', 'description', 'website_url', 'phone', 'location_info']
        read_only_fields = ['id']


class RegistrationDeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationDeadline
        fields = ['id', 'state', 'election_year', 'registration_deadline', 'election_date', 'notes']
        read_only_fields = ['id']
