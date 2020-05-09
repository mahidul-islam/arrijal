from django.urls import path

from . import views

app_name = "chemistry"
urlpatterns = [
    path("", views.chemistry, name="chemistry"),
    path("tankofnet", views.tankofnet, name="tankofnet"),
    path("tank", views.tank, name="experimentTank"),
    path("oxygen", views.oxygen, name="oxygen"),
    path("carbon", views.carbon, name="carbon"),

]
