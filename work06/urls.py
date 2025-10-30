from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("reiwa/", views.reiwa_view, name="reiwa"),
]
