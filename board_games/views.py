from django.shortcuts import render

def index(request):
    """The home page Board game."""
    return render(request, 'board_games/index.html')
    