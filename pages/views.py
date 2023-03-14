from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from django.views.generic import TemplateView

from django.core.mail import send_mail


from django.urls import reverse, path
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

import traceback
from django.contrib.auth.views import LoginView
from django.contrib import messages


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about_us.html"


def home(request):
    context = {}
    if request.user.is_authenticated:
        context["welcome_message"] = "Welcome, " + request.user.username + "!"
    return render(request, "pages/home.html", context)


def contact_form(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        send_mail(
            "Contact form submission",
            message,
            email,
            ["recipient@example.com"],
            fail_silently=False,
        )
        return redirect("contact_success")
    return render(request, "registration/contact/contact_form.html")


def contact_success(request):
    return render(request, "accounts/registration/contact/contact_success.html")


@login_required
def muns_scoring_sheet(request):
    if request.user.is_authenticated:
        context["welcome_message"] = "Welcome, " + request.user.username + "!"
    else:
        messages.warning(request, "You need to log in to use the MUNS Scoring Sheet.")
