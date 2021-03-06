from django.urls import path

from . import views

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>/",  views.detail, name="title"),
    path("search/", views.search, name="search"),
    path("search/<str:query>/", views.result, name="result"),
    path("create/", views.create, name="create"),
    path("edit/<str:entry>", views.edit, name="edit"),
    path("edit", views.edit, name="edit"),
    path("random", views.random_page, name="random"),
]
