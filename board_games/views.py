from django.shortcuts import render
from .models import Game

def index(request):
    """The home page Board game."""
    return render(request, 'board_games/index.html')

def games(request):
    """Show all games."""
    games = Game.objects.order_by('date_added')
    context = {'games':games}
    return render( request, 'board_games/games.html', context)

