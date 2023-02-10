from django.urls import path
from . import views
from django.urls import reverse, reverse_lazy


urlpatterns = [
    path("menu/", views.menu_view, name="menu"),
]
