from django.urls import path

from . import views

app_name = "isnad"
urlpatterns = [
    path("", views.isnad, name="isnad"),
    path("isgraph", views.igraph, name="isgraph"),
    path("graph1", views.graph1, name="graph1"),
    path("graph2", views.graph2, name="graph2"),
    path("graph3", views.graph3, name="graph3"),
    path("load", views.load, name="load"),

]
