from django.urls import path

from . import views

app_name = "map"
urlpatterns = [
    path("", views.map, name="map"),
    path("firstMap", views.firstMap, name="firstMap"),
    path("bangladesh", views.bangladesh, name="bangladesh"),
    path("d3", views.d3, name="d3"),
    path("povertymap", views.povertymap, name="povertymap"),
    path("bdgeojson", views.bdgeojson, name="bdgeojson"),
    path("markermap", views.markermap, name="markermap"),
    path("mymarker", views.mymarker, name="mymarker"),
    path("mapSlider", views.mapSlider, name="mapSlider"),
    path("debug", views.debug, name="debug"),
]
