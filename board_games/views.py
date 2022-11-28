from django.shortcuts import render, redirect
from .models import Game
from .forms import GameForm

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
    