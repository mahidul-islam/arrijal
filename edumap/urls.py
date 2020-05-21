from django.urls import path

from . import views

app_name = "edumap"
urlpatterns = [
    path("", views.edumap, name="edumap"),
    path("firstMap", views.firstMap, name="firstMap"),
]