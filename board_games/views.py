
from django.shortcuts import render, redirect
from .models import Game
from .forms import GameForm
from .forms import BorrowForm


def index(request):
    """The home page Board game."""
    return render(request, 'board_games/index.html')

def new_game(request):
    """Add a new game."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = GameForm()
    else:
        # POST data submitted; process data
        form = GameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_games:games')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'board_games/new_game.html, context')
    
def game(request, game_id):
    """Show all games."""
    game = Game.objects.get(id=game_id)
    gamers = Game.objects.order_by('name')
    context = {'game':game, 'gamers':gamers}
    return render( request, 'board_games/game.html', context)

def games(request):
    """Show all games."""
    games = Game.objects.order_by('name')
    context = {'games': games }
    return render(request, 'board_games/games.html', context)

def new_borrow(request, game_id):
    """Add a new borrow info on a game."""
    game = Game.objects.get(id=game_id)
    if request.method != 'POST':
        form = BorrowForm()
    else:
        form = BorrowForm(data=request.POST)
        if form.is_valid():
            new_borrow = form.save(commit=False)
            new_borrow.game=game
            new_borrow.save()
            return redirect('board_games:game', game_id=game_id)
    # Display a blank or invalid form.
    context={'game':game,'form':form}
    return render(request, 'board_games/new_borrow.html', context)