"""Defines URL patterns for board_games."""

from django.urls import path

from . import views

app_name = 'board_games'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for adding a new game
    path('new_game/', views.new_game, name='new_game'),
    #Page that shows all games.
    path('games/', views.game , name='games'),
    #Detail page for a single game 
    path('games/<int:game_id>/', views.game, name='game'),
]