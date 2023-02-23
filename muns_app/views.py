# views.py
from django.shortcuts import render, redirect
from .forms import (
    WordsLearningSubtestForm,
    WordsLearningSubtestTrial2Form,
    WordsLearningSubtestTrial3Form,
)
from .models import Protocol


def new_protocol_view(request):
    # Retrieve all Protocol objects from the database
    protocols = Protocol.objects.all()

    # Render the 'protocols.html' template with the list of protocols
    return render(request, "new_protocol.html", {"protocols": protocols})


def create_protocol(request):
    if request.method == "POST":
        # If the request method is POST, extract the protocol data from the form
        gender = request.POST["gender"]
        age = request.POST["age"]
        country = request.POST["country"]
        city = request.POST["city"]
        ethnicity = request.POST["ethnicity"]
        education = request.POST["education"]
        fluency = request.POST["fluency"]
        language = request.POST["language"]
        native_language = request.POST["native_language"]
        occupation = request.POST["occupation"]
        income = request.POST["income"]
        medical_history = request.POST["medical_history"]
        medication_use = request.POST["medication_use"]
        drug_history = request.POST["drug_history"]
        alcohol_history = request.POST["alcohol_history"]
        covid = request.POST["covid"]
        participant_type = request.POST["participant_type"]

        # Create a new Protocol object with the extracted data
        protocol = Protocol.objects.create(
            gender=gender,
            age=age,
            country=country,
            city=city,
            ethnicity=ethnicity,
            education=education,
            fluency=fluency,
            language=language,
            native_language=native_language,
            occupation=occupation,
            income=income,
            medical_history=medical_history,
            medication_use=medication_use,
            drug_history=drug_history,
            alcohol_history=alcohol_history,
            covid=covid,
            participant_type=participant_type,
        )

        # Redirect to the 'protocols' page to see the newly created protocol
        return HttpResponse(
            '<h1>Protocol created!</h1><a href="/protocols">Back to Protocols</a>'
        )

    else:
        # If the request method is GET, render the 'new_protocol.html' template
        return render(request, "new_protocol.html")


def protocols_view(request):
    protocols = ['Protocol 1', 'Protocol 2', 'Protocol 3']
    context = {'protocols': protocols}
    return render(request, 'protocols.html', context)


def words_learning_subtest_view(request):
    if request.method == "POST":
        form = WordsLearningSubtestForm(request.POST)
        form2 = WordsLearningSubtestTrial2Form(request.POST)
        form3 = WordsLearningSubtestTrial3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("words_learning_subtest")
        if form2.is_valid():
            form2.save()
            return redirect("words_learning_subtest")
        if form3.is_valid():
            form3.save()
            return redirect("words_learning_subtest")
    else:
        form = WordsLearningSubtestForm()
        form2 = WordsLearningSubtestTrial2Form()
        form3 = WordsLearningSubtestTrial3Form()

    context = {"form": form, "form2": form2, "form3": form3}
    return render(request, "words_learning_subtest.html", context)


def success_view(request):
    return render(request, "success.html")


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
