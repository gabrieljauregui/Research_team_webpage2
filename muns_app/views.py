#views.py
from django.shortcuts import render, redirect
from .forms import words_memory_subtest

# muns_app/views.py

def words_memory_subtest_view(request):
    if request.method == 'POST':
        form = words_memory_subtest(request.POST)
        if form.is_valid():
            # Handle the form submission
            # ...
            return redirect('success')
    else:
        form = words_memory_subtest()
    return render(request, 'muns_app/words_memory_subtest.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')


def menu_view(request):
    menu_items = [
        {"name": "Home", "url_name": "home"},
        {"name": "About", "url_name": "about"},
        {"name": "Contact", "url_name": "contact"},
    ]
    return render(request, "menu.html", {"menu_items": menu_items})

""""
def forgot_password(request):
    if request.method == "POST":
        # Process the form submission
        email = request.POST["email"]
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(
                request, "No user with the provided email address was found."
            )
            return redirect("forgot_password")
        # Send password reset email to the user
        user.send_password_reset_email()
        messages.success(
            request,
            "A password reset email has been sent to the provided email address.",
        )
        return redirect("login")
    else:
        return render(request, "forgot_password.html")


def forgot_password(request):
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            # Send password reset email
            pass
        else:
            return render(request, "forgot_password.html", {"form": form})
    else:
        form = ForgotPasswordForm()
        return render(request, "forgot_password.html", {"form": form})


def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "An email has been sent to you with instructions to reset your password.",
            )
            return redirect(reverse("login"))
    else:
        form = PasswordResetRequestForm()
    return render(request, "authenticate/password_reset_form.html", {"form": form})

""" 