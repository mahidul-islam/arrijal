from django.urls import path

from . import views

app_name = "physics"
urlpatterns = [
    path("", views.physics, name="physics"),
    path("firstGame/", views.firstGame, name="firstGame"),
]
