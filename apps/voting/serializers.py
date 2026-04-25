from rest_framework import serializers
from .models import VotingProcedure, VotingMethod

class VotingProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotingProcedure
        fields = ['id', 'title', 'description', 'state', 'category', 'content', 'is_published', 'created_at']
        read_only_fields = ['id', 'created_at']


class VotingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotingMethod
        fields = ['id', 'name', 'description', 'pros', 'cons', 'availability_states', 'created_at']
        read_only_fields = ['id', 'created_at']
