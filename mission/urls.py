

from django.urls import path
from .views import MissionsView 

app_name = "mission" 

urlpatterns = [
    path("", MissionsView.as_view(), name = "missions"),
]



