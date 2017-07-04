from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

from .forms import (LoginForm, RegisterForm, TravellerProfileForm, EmployeeProfileForm)


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

            user.refresh_from_db()  # Just added in case, no effect observed

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


def profile_edit_view(request, pk):

    if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser or (str(request.user.pk) == pk)):
        # pk received from url pattern is a str, hence need to convert request.user's pk also to str

        user = get_object_or_404(User, pk=pk)
        profile_instance = user.profile

        if profile_instance.user_type == 1:
            form_class = TravellerProfileForm
        else:
            form_class = EmployeeProfileForm

        if request.method == "POST":
            form = form_class(request.POST, request.FILES, instance=profile_instance)
            if form.is_valid():
                profile_instance = form.save(commit=False)
                profile_instance.save()

                return redirect('homepage')
        else:
            form = form_class(instance=profile_instance)

        return render(request, 'accounts/user_form.html', {
            'title_message': 'Edit Profile',
            'submit_message': 'Save',
            'form': form,
        })

    else:
        raise PermissionDenied


def profile_detail_view(request, pk):

    if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser or (str(request.user.pk) == pk)):
        # pk received from url pattern is a str, hence need to convert request.user's pk also to str

        user = get_object_or_404(User, pk=pk)
        if user.profile.user_type == 1:
            is_traveller = True
        else:
            is_traveller = False

        return render(request, 'accounts/profile_detail.html', {
            'user': user,
            'is_traveller': is_traveller,
        })

    else:
        raise PermissionDenied
