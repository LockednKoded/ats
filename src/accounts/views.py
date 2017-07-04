from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import (LoginForm, RegisterForm,)


def login_view(request):
    title_message = "Login"
    submit_message = "Login"

    if not request.user.is_authenticated():
        if request.method == "POST":
            form = LoginForm(request.POST)

            if form.is_valid():
                username = form.cleaned_data.get("username")
                raw_password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=raw_password)
                login(request, user)

                return redirect("homepage")  # can also write return redirect("/")

        else:
            form = LoginForm()

        return render(request, 'accounts/user_form.html', {
            'title_message': title_message,
            'submit_message': submit_message,
            'form': form,
        })

    else:
        return redirect("homepage")


def logout_view(request):
    logout(request)
    return redirect("homepage")


def register_view(request):
    title_message = "Registration"
    submit_message = "Register"

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data.get("password")
            user.set_password(raw_password)
            user.save()

            # user need to be save before this, signal creates profile on save
            user_type = form.cleaned_data.get("register_type")
            user.profile.user_type = user_type
            user.profile.save()

            new_user = authenticate(username=user.username, password=raw_password)
            login(request, new_user)

            return redirect('homepage')

    else:
        form = RegisterForm()

    return render(request, 'accounts/user_form.html', {
        'title_message': title_message,
        'submit_message': submit_message,
        'form': form,
    })
