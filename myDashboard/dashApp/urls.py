from django.urls import path
from .views import *

urlpatterns = [
    path("",top,name="top"),
    path("getlink",get_aws_rss),
    path("downdetector",get_downdetector),
]
