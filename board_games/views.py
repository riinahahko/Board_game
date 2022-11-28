from django.shortcuts import render
from .models import Game

def index(request):
    """The home page Board game."""
    return render(request, 'board_games/index.html')

def game(request, game_id):
    """Show all games."""
    game = Game.objects.get(id=game_id)
    gamers = Game.objects.order_by('date_added')
    context = {'game':game, 'gamers':gamers}
    return render( request, 'board_games/games.html', context)

