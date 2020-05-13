from django.urls import path

from . import views

app_name = "chemistry"
urlpatterns = [
    path("", views.chemistry, name="chemistry"),
    path("tank", views.tank, name="tank"),
    path("oxygen", views.oxygen, name="oxygen"),
    path("molecule", views.molecule, name="molecule"),

]
