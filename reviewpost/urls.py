from django.contrib import admin
from django.urls import path
from .views import signupview, loginview, listview

urlpatterns = [
    path('signup/', signupview, name="signup"),
    path("login/", loginview, name="login"),
    path("list/", listview, name="list")
]
