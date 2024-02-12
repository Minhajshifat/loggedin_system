from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash


# Create your views here.
def user_register(request):
    if request.method == "POST":
        register_form = forms.registeruser(request.POST)
        if register_form.is_valid():
            messages.success(request, "Account is created successfully.")
            register_form.save()
            return redirect("home")
    else:
        register_form = forms.registeruser()
    return render(request, "registation.html", {"form": register_form})


def user_login(request):
    if request.method == "POST":
        loginform = AuthenticationForm(request, request.POST)
        if loginform.is_valid():
            user_name = loginform.cleaned_data["username"]
            user_pass = loginform.cleaned_data["password"]
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, "logged in successfully.")
                login(request, user)
                return redirect("home")
            else:
                messages.warning(request, "user information inccorrect")
                return redirect("register")
    else:
        loginform = AuthenticationForm()
    return render(request, "registation.html", {"form": loginform})


def user_logout(request):
    logout(request)
    messages.success(request, "Log out successfully.")
    return redirect("home")


def pass_change(request):
    if request.method == "POST":
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password Updated Successfully")
            update_session_auth_hash(request, form.user)
            return redirect("profile")

    else:
        form = SetPasswordForm(user=request.user)
    return render(request, "pass_change.html", {"form": form})


def pass_change2(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password updated succesfully")
            update_session_auth_hash(request, form.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "pass_change.html", {"form": form})


def profile(request):
    return render(request, "profile.html")
