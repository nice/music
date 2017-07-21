from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

RATING_CHOICES = (
    (1, '1 - Very Poor'),
    (2, '2 - Poor'),
    (3, '3 - Average'),
    (4, '4 - Good'),
    (5, '5 - Very Good'),
)


class Track(models.Model):
    title = models.CharField(max_length=200)
    genres = models.ManyToManyField('Genre')
    rating = models.IntegerField(
            default = 1,
            validators = [
                MinValueValidator(1),
                MaxValueValidator(5)
            ],
            choices = RATING_CHOICES
        )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
