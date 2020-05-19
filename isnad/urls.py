from django.urls import path
from . import views

app_name = "isnad"
urlpatterns = [
    path("graph", views.graph, name="graph"),

]
