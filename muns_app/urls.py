# urls.py
from django.urls import path
from .views import words_memory_subtest_view, success_view, menu_view

urlpatterns = [
    path('words-memory-subtest/', words_memory_subtest_view, name='words_memory_subtest'),
    path('success/', success_view, name='success'),
    path('menu/', menu_view, name='menu'),
]
