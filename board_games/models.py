from django.db import models

class Board_game(models.Model):
    """A games the gamers own currently"""
    name = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name
