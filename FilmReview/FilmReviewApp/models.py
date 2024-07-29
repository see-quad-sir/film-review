from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="posters/")
    star_rating_avg = models.FloatField(default=0)


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    star_rating = models.IntegerField()
