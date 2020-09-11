from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_name>", views.title, name="title"),
    path("search", views.search, name="search"),
    path("New_Page", views.New_Page, name="New_Page"),
    path("Edit_Page/<str:name>", views.Edit_Page, name="Edit_Page"),
    path("Random_Page", views.Random_Page, name="Random_Page"),

]
