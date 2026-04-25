from rest_framework import serializers
from .models import Candidate, CandidatePolicy, CandidateComparison

class CandidatePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidatePolicy
        fields = ['id', 'issue', 'position', 'source_url']
        read_only_fields = ['id']


class CandidateSerializer(serializers.ModelSerializer):
    policies = CandidatePolicySerializer(many=True, read_only=True)

    class Meta:
        model = Candidate
        fields = ['id', 'name', 'position', 'party', 'bio', 'image', 'website', 'email', 'phone', 
                  'office_sought', 'district', 'state', 'election_year', 'policies', 'created_at']
        read_only_fields = ['id', 'created_at']


class CandidateComparisonSerializer(serializers.ModelSerializer):
    candidates = CandidateSerializer(many=True, read_only=True)
    candidate_ids = serializers.PrimaryKeyRelatedField(
        queryset=Candidate.objects.all(),
        write_only=True,
        many=True,
        source='candidates'
    )

    class Meta:
        model = CandidateComparison
        fields = ['id', 'candidates', 'candidate_ids', 'position', 'election_year', 'created_by_user', 'created_at']
        read_only_fields = ['id', 'created_at']
