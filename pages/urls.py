from django.urls import include, path
from .views import HomePageView, AboutPageView # new
from . import views

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('contact/', include('accounts.urls')),
    ]
