

from django.urls import path
from .views import HomeView, FAQView 

app_name = "navigation" 

urlpatterns = [
    path("", HomeView.as_view(), name = "home"),
    path("faq/", FAQView.as_view(), name = "faq"),
]



