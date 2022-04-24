from django.db import models


class Polygon(models.Model):
    name = models.CharField(max_length=255)
    num_sides = models.PositiveIntegerField()

    def __str__(self):
        return self.name
