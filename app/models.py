from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Track(models.Model):
    title = models.TextField(max_length=200)
    genres = models.ManyToManyField('Genre')
    rating = models.IntegerField(
            default = 1,
            validators = [
                MinValueValidator(1),
                MaxValueValidator(5)
            ]
        )

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.TextField(max_length=200)

    def __str__(self):
        return self.name
