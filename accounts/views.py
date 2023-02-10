import traceback

from django.shortcuts import render, redirect
from django.urls import reverse, path, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic.edit import CreateView
from django import forms
from .forms import MyUserCreationForm, LoginForm
from .models import MyUser
from django.contrib.messages import success, info



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
    

class MyLoginView(LoginView):
    template_name = "registration/login.html"

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            return redirect("home")
        messages.success(self.request, f"Hello, {form.user.first_name}!")
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)


def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("home")



class MyUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    last_name = forms.CharField(max_length=50)
    job = forms.CharField(max_length=100)
    educational_achievement = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    objectives = forms.CharField(widget=forms.Textarea)

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = UserCreationForm.Meta.fields + (
            "email",
            "username",
            "age",
            "last_name",
            "job",
            "educational_achievement",
            "description",
            "objectives",
            "password1",
            "password2",
        )


class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "signup.html"

    def form_valid(self, form):
        try:
            # Process the form data and create a new user
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            age = form.cleaned_data["age"]
            job = form.cleaned_data["job"]
            educational_achievement = form.cleaned_data["educational_achievement"]
            description = form.cleaned_data["description"]
            objectives = form.cleaned_data["objectives"]
            password = form.cleaned_data["password1"]
            username = form.cleaned_data["username"]
            # Create a new user using the form data
            user = MyUser.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
            user.age = age
            user.job = job
            user.educational_achievement = educational_achievement
            user.description = description
            user.objectives = objectives
            user.save()
            login(self.request, user)
            return redirect(self.success_url)
        except Exception as e:
            traceback.print_exc()
            messages.error(self.request, "An error occurred. Please try again.")
            return redirect("signup")


def contact_form(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        send_mail(
            "Contact form submission",
            message,
            email,
            ["gabriel.jaur@gmail.com"],
            fail_silently=False,
        )
        return redirect("contact_success")
    return render(request, "registration/contact/contact_form.html")


def contact_success(request):
    return render(request, "registration/contact/contact_success.html")
