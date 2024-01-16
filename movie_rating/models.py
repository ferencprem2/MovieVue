from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release = models.DateField()
    poster_image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    average_rating = models.FloatField(null=True, blank=True, default=0.0)

    def __str__(self):
        return self.title

class Rating(models.Model):
    choices = [ (1,1), (2,2), (3,3), (4,4), (5,5) ]
    value = models.IntegerField(choices=choices)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

@receiver(post_save, sender=Rating)
def updateMovieRating(sender, instance, **kwargs):
    # instance = az a szavazat amit leadtunk utoljára
    movie_instance = Movie.objects.get(id=instance.movie.id)

    relevant_ratings = Rating.objects.filter(movie = movie_instance)

    sum = 0
    count = 0
    for rating in relevant_ratings:
        sum += rating.value
        count += 1

    movie_instance.average_rating = sum / count
    movie_instance.save()
