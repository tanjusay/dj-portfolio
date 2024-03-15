#main/urls.py manually added

from .views import *
from django.urls import path

urlpatterns = [
    path("", index, name="index"),
    path("profile/", profile, name="profile"),
    path("projects/", projects, name="projects"),
    path("contact/", contact, name="contact"),
]

