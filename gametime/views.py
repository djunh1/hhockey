from django.shortcuts import render, get_object_or_404
from .models import Game
from django.views.generic import ListView

class GameListView(ListView):
    queryset = Game.gamelist.all()
    context_object_name = 'games'
    paginate_by = 5
    template_name = 'games/list.html'
