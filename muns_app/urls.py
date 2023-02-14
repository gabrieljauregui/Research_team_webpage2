# urls.py
from django.urls import path
from .views import words_learning_subtest_view, success_view, menu_view

urlpatterns = [
    path('words_learning_subtest/', words_learning_subtest_view, name='words_learning_subtest'),
    path('success/', success_view, name='success'),
    path('menu/', menu_view, name='menu'),
]
