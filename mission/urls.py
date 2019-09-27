

from django.urls import path
from .views import MissionsView 

app_name = "mission" 

urlpatterns = [
        path("<slug:slug>/", MissionsView.as_view(), name = "missions"),
]



