# urls.py
from django.urls import path
from .views import (
    words_learning_subtest_view,
    success_view,
    menu_view,
    new_protocol_view,
    protocols_view,
)

urlpatterns = [
    path("words_learning_subtest/", words_learning_subtest_view, name="words_learning_subtest"),
    path("success/", success_view, name="success"),
    path("menu/", menu_view, name="menu"),
    path("new_protocol/", new_protocol_view, name="new_protocol"),
    path("protocols/", protocols_view, name="protocols"),
]
