from django.urls import path

from . import views

app_name = "isnad"
urlpatterns = [
    path("", views.isnad, name="isnad"),
    path("sgraph", views.sgraph, name="sgraph"),
    path("igraph", views.igraph, name="igraph"),
    path("graph1", views.graph1, name="graph1"),
    path("graph2", views.graph2, name="graph2"),
    path("graph3", views.graph3, name="graph3"),
    path("graph4", views.graph4, name="graph4"),
    path("graph5", views.graph5, name="graph5"),

    path("sload", views.sload, name="sload"),
    path("iload", views.iload, name="iload"),

]
