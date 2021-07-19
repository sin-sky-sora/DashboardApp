from django.urls import path
from .views import *

urlpatterns = [
    path("",top,name="top"),
    path("getlink",get_aws_rss,name="aws"),
    path("downdetector",get_downdetector),
]
