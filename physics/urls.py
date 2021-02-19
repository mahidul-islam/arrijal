from django.urls import path

from . import views

app_name = "physics"
urlpatterns = [
    path("", views.physics, name="physics"),
    path("firstGame/", views.firstGame, name="firstGame"),
    path("mod2d/", views.mod2d, name="mod2d"),
    path("threed/", views.threed, name="threed"),
    path("threed_mobile/", views.threed_mobile, name="threed_mobile"),
]
