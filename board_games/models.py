from django.db import models

class Game(models.Model):
    """A games the gamers own currently"""
    name = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class Borrow(models.Model):
  my_borrow = models.TextField()
  game = models.ForeignKey(Game, on_delete=models.CASACADE)
  date_added = models.DateTimeField(auto_now_add=True)
  date_borrowed = models.DateTimeField(auto_add=True)
  
  def __str__(self):
    return f"{self.my_borrow[:50]}..."


