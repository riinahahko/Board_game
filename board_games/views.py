
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Game
from .forms import GameForm
from .forms import BorrowForm
from django.contrib.auth.decorators import login_required


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
    
@login_required
def game(request, game_id):
    """Show all games."""
    game = Game.objects.get(id=game_id)
    gamers = Game.objects.order_by('name')
    context = {'game':game, 'gamers':gamers}
    return render( request, 'board_games/game.html', context)

@login_required
def games(request):
    """Show all games."""
    games = Game.objects.order_by('name')
    context = {'games': games }
    return render(request, 'board_games/games.html', context)

@login_required
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

            return redirect('board_games/new_borrow.html', context)

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        #Process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Log the user in and then redirect to home page
            login(request, new_user)
            return redirect('board_games:index')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)

            return redirect('board_games:game', game_id=game_id)
    # Display a blank or invalid form.
    context={'game':game,'form':form}
    return render(request, 'board_games/new_borrow.html', context)

