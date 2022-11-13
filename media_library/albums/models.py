from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Album(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    date_acquired = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.artist}"
