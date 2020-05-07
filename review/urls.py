from django.urls import path

from . import views

app_name = "review"
urlpatterns = [
    path("", views.review, name="review"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("edit/<int:id>/", views.edit, name="edit"),
    path("readmore/<int:id>/", views.readmore, name="readmore"),

]
