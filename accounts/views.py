from django.shortcuts import redirect, render
from django.contrib import auth

from accounts.forms import RegistrationForm
from accounts.models import Account

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            username = email.split("@")[0]

            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password
            )
            user.phone_number = phone_number
            user.save()

    form = RegistrationForm()
    return render(request, "register.html", context={"form": form})

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, password)
        user = auth.authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    return render(request, "index.html")