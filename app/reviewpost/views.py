from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import ReviewModel
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


def signupview(request):
    if request.method != "POST":
        return render(request, "signup.html", {})
    print("POST method")
    username_data = request.POST.get("username_data")
    password_data = request.POST.get("password_data")
    try:
        user = User.objects.create_user(
            username_data, "", password_data)
        return render(request, "login.html", {})
    except IntegrityError:
        return render(request, "signup.html", {"error": "このユーザは既に登録されています   "})


def loginview(request):
    if request.method != "POST":
        return render(request, "login.html")
    username_data = request.POST.get("username_data")
    password_data = request.POST.get("password_data")
    user = authenticate(request, username=username_data,
                        password=password_data)
    if user is not None:
        login(request, user)
        return redirect("list")
    else:
        return redirect("login")


@login_required
def listview(request):
    object_list = ReviewModel.objects.all()
    return render(request, "list.html", {"object_list": object_list})


@login_required
def detailview(request, pk):
    object = ReviewModel.objects.get(pk=pk)
    return render(request, "detail.html", {"object": object})


class CreateClass(CreateView):
    template_name = "create.html"
    model = "ReviewModel"
    fields = ("title", "content", "author", "images", "evaluation")
    success_url = reverse_lazy("list")


def logoutview(request):
    logout(request)
    return redirect("login")


def evaluationview(request, pk):
    post = ReviewModel.objects.get(pk=pk)
    author_name = request.user.get_username()+str(request.user.id)
    if author_name in post.useful_review_record:
        return redirect("list")
    else:
        post.useful_review += 1
        post.useful_review_record += author_name
        post.save()
        return redirect("list")
