from django.urls import path

from . import views

app_name = "edumap"
urlpatterns = [
    path("", views.edumap, name="edumap"),
    path("firstMap", views.firstMap, name="firstMap"),
    path("bangladesh1", views.bangladesh, name="bangladesh1"),
    path("bangladesh0", views.bangladesh0, name="bangladesh0"),

]
