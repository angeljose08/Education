from django.contrib import admin
from .models import Candidate, CandidatePolicy, CandidateComparison

class CandidatePolicyInline(admin.TabularInline):
    model = CandidatePolicy
    extra = 1


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'party', 'state', 'election_year', 'is_published']
    list_filter = ['position', 'state', 'election_year', 'party', 'is_published']
    search_fields = ['name', 'position', 'office_sought']
    inlines = [CandidatePolicyInline]


@admin.register(CandidatePolicy)
class CandidatePolicyAdmin(admin.ModelAdmin):
    list_display = ['candidate', 'issue', 'created_at']
    search_fields = ['candidate__name', 'issue']


@admin.register(CandidateComparison)
class CandidateComparisonAdmin(admin.ModelAdmin):
    list_display = ['position', 'election_year', 'created_by_user']
    list_filter = ['position', 'election_year']
