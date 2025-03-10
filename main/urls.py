from django.urls import path, include
from .views import *

urlpatterns = [
    path("", Main.as_view(), name="main"),
    path("testAPI/", TestAPIForm.as_view(), name="test"),
    path("achievements/", Achievements.as_view(), name="achievements"),
    path("myActivities/", MyActivities.as_view(), name="myActivities"),
    path("addAchievement/", AddAchievements.as_view(), name="addAchievements"),
]