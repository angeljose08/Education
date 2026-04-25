from django.contrib import admin
from .models import RegistrationRequirement, RegistrationMethod, RegistrationDeadline

@admin.register(RegistrationRequirement)
class RegistrationRequirementAdmin(admin.ModelAdmin):
    list_display = ['state', 'requirement', 'created_at']
    list_filter = ['state', 'requirement']
    search_fields = ['state', 'description']


@admin.register(RegistrationMethod)
class RegistrationMethodAdmin(admin.ModelAdmin):
    list_display = ['state', 'method', 'created_at']
    list_filter = ['state', 'method']
    search_fields = ['state', 'description']


@admin.register(RegistrationDeadline)
class RegistrationDeadlineAdmin(admin.ModelAdmin):
    list_display = ['state', 'election_year', 'registration_deadline', 'election_date']
    list_filter = ['election_year', 'state']
    search_fields = ['state']
    ordering = ['-election_year', 'state']
