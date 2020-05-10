from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.blogpage, name="blog"),
    path('category-dao/<category_id>/', views.category_dao, name='category-dao'),
    path("search/", views.search, name="search"),

    #path("delete/<int:id>/", views.delete, name="delete"),
    #path("edit/<int:id>/", views.edit, name="edit"),
    #path("readmore/<int:id>/", views.readmore, name="readmore"),
]
