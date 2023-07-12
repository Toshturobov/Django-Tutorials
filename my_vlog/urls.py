from django.urls import path 

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("gaming/", views.gaming, name="gaming"),
    path("vlogs/", views.vlogs, name="vlogs"),
    path("movies/", views.movies, name="movies"),
    path("podcast/", views.podcast, name="podcats"),
    path("reacts/", views.reacts, name="reacts"),
    path("xabar/", views.xabar, name="xabar"),
]