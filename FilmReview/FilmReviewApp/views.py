from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Movie, User


# Create your views here.
def index(request):
    movie_list = Movie.objects.all()
    context = {"movie_list": movie_list}
    return render(request, "FilmReviewApp/index.html", context)


def user(request):
    if request.method == "POST":
        movie_list = Movie.objects.all()
        if "login" in request.POST:
            user_name = request.POST["username"]
            password = request.POST["password"]
            user = User.objects.get(user_name=user_name, password=password)
            context = {"movie_list": movie_list, "user": user}
            return render(request, "FilmReviewApp/main.html", context)
        elif "signup" in request.POST:
            user_name = request.POST["username"]
            password = request.POST["password"]
            user = User(user_name=user_name, password=password)
            user.save()
            context = {"movie_list": movie_list, "user": user}
            render(request, "FilmReviewApp/main.html", context)
    return HttpResponseRedirect(reverse("FilmReviewApp:index"))


def logout(request):
    return HttpResponseRedirect(reverse("FilmReviewApp:index"))


def movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    context = {"movie": movie}
    return render(request, "FilmReviewApp/movie.html", context)
