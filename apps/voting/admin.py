from django.contrib import admin
from .models import VotingProcedure, VotingMethod

@admin.register(VotingProcedure)
class VotingProcedureAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'state', 'is_published', 'created_at']
    list_filter = ['category', 'state', 'is_published']
    search_fields = ['title', 'description']
    list_editable = ['is_published']


@admin.register(VotingMethod)
class VotingMethodAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name', 'description']
