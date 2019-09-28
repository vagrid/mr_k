

from django.shortcuts import render
from django.views.generic import View
from .models import Location, Mission

from collections import OrderedDict

class MissionsView(View):
    """
    """
     
    #
    def get(self, request, slug):
        """
        """
        # 
        template_name           = "mission/missions.html"
        #
        location                = slug 
        # 
        locations               = Location.objects.all()
        # 
        missions                = Mission.objects.all()
        #
        mission_gauge = dict()
        # 
        for mission in missions:
            mission_gauge[mission.title]                = OrderedDict()#dict()
            mission_gauge[mission.title]["difficulty"]  = mission.difficulty 
            mission_gauge[mission.title]["logic"]       = mission.logic 
            mission_gauge[mission.title]["handling"]    = mission.handling 
            mission_gauge[mission.title]["search"]      = mission.search 
        #
        mission_information = dict()
        # 
        for mission in missions:
            mission_information[mission.title]                = OrderedDict()#dict()
            mission_information[mission.title]["success"]     = mission.success 
            mission_information[mission.title]["players"]     = [mission.min_players, mission.max_players] 
            mission_information[mission.title]["age"]         = [mission.min_age, mission.max_age] 
            mission_information[mission.title]["duration"]    = mission.duration 
        # 
        context             = {"location":location, "locations":locations, "missions":missions, "gauge":mission_gauge, "information":mission_information, "range":range(1,6)} 
        #
        return render(request, template_name, context)

