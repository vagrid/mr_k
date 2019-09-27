

from django.shortcuts import render
from django.views.generic import View
from .models import Location, Mission

class MissionsView(View):
    """
    """
     
    #
    def get(self, request, slug):
        """
        """
        # 
        template_name       = "mission/missions.html"
        #
        location            = slug 
        # 
        locations           = Location.objects.all()
        # 
        missions            = Mission.objects.all()
        #
        mission_description = []
        # 
        context             = {"location":location, "locations":locations, "missions":missions, "description":mission_description} 
        #
        return render(request, template_name, context)

