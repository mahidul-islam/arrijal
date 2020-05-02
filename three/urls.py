from django.urls import path

from . import views

app_name = "three"
urlpatterns = [
    path("", views.three, name="three"),
    path("hydrogen", views.hydrogen, name="hydrogen"),
    path("experiment", views.experiment, name="experiment"),
    path("carbonDiOxide", views.carbonDiOxide, name="carbonDiOxide"),
    path("water", views.water, name="water"),
]
