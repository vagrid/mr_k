
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

    #
    def get_prepopulated_fields(self, request, obj = None):
        """
        """
        return {"slug": ("title",)}
