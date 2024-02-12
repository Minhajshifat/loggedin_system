from django.urls import path, include
from . import views

urlpatterns = [
    path("register", views.user_register, name="register"),
    path("login", views.user_login, name="login"),
    path("logout", views.user_logout, name="logout"),
    path("passchange", views.pass_change, name="passchange"),
    path("profile", views.profile, name="profile"),
    path("passchange2", views.pass_change2, name="passchange2"),
]
