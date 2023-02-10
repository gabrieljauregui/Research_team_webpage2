from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import MyLoginView
from django.contrib.auth.views import LogoutView
from .views import logout_view

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_view'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    
]

from django.urls import path
from .views import login_view