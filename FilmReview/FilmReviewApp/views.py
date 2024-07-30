from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ReviewForm
from .models import Movie, Review, User


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


def movie(request, movie_id, user_id):
    movie = Movie.objects.get(pk=movie_id)
    reviews = Review.objects.filter(movie_id=movie_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            if not Review.objects.filter(movie_id=movie_id, user_id=user_id).exists():
                review = Review()
                review.movie = movie
                review.user = User.objects.get(pk=user_id)
                review.review = form.cleaned_data["review"]
                review.star_rating = form.cleaned_data["rating"]
                num_reviews = Review.objects.filter(movie_id=movie_id).count()
                rating_diff = review.star_rating - movie.star_rating_avg
                movie.star_rating_avg += rating_diff / (num_reviews + 1)
                review.save()
                movie.save()
            return HttpResponseRedirect(
                reverse("FilmReviewApp:movie", args=(movie_id, user_id))
            )
    else:
        form = ReviewForm()

    context = {"movie": movie, "reviews": reviews, "user_id": user_id, "form": form}
    return render(request, "FilmReviewApp/movie.html", context)


def review(request, movie_id):
    if request.method == "POST":
        movie = Movie.objects.get(pk=movie_id)
        user = User.objects.get(pk=request.POST["user_id"])
        review = request.POST["review"]
        star_rating = request.POST["star_rating"]
        review = Review(
            movie=movie,
            user=user,
            review=review,
            star_rating=star_rating,
        )
        num_reviews = Review.objects.filter(movie_id=movie_id).count()
        rating_diff = star_rating - movie.star_rating_avg
        movie.star_rating_avg += rating_diff / (num_reviews + 1)
        review.save()
        movie.save()
        return HttpResponseRedirect(
            reverse("FilmReviewApp:movie", args=(movie_id, user.id))
        )
    return HttpResponseRedirect(reverse("FilmReviewApp:index"))
