from django.db import models

class Game(models.Model):
    """A games the gamers own currently"""
    name = models.CharField(max_length=200)
    game_owner = models.TextField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name
class Gamers(models.Model):
    """Board game players that can loan the games."""
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player_name = models.TextField()

    class Meta:
        verbose_name_plural = 'gamers'
    
    def __str__(self):
        return f"{self.game[:50]}..."
