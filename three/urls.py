from django.urls import path

from . import views

app_name = "three"
urlpatterns = [
    path("", views.three, name="three"),
    path("hydrogen", views.hydrogen, name="hydrogen"),
    path("experiment", views.hydrogen, name="experiment"),
]
