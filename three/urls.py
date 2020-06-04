from django.urls import path

from . import views

app_name = "three"
urlpatterns = [
    path("", views.three, name="three"),
    path("equations", views.equations, name="equations"),
    path("experiment", views.experiment, name="experiment"),
    path("aromaticChart", views.aromaticChart, name="aromaticChart"),
    path("aliphaticChart", views.aliphaticChart, name="aliphaticChart"),
    path("tankofnet", views.tankofnet, name="tankofnet"),
    path("tank", views.tank, name="experimentTank"),
    path("guiexample", views.guiexample, name="guiexample"),
    path("base", views.base, name="base"),
    path("periodic", views.periodic, name="periodic"),
    path("alcohol", views.alcohol, name="alcohol"),
    path("molecules", views.molecules, name="molecules"),
]
