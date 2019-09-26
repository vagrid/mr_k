
from django.contrib import admin
from .models import Location, Mission


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """
    """
    list_display = ["name"]

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    """
    """
    list_display = ["title"]
