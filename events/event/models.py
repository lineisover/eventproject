from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
