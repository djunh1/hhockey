from django.shortcuts import render, get_object_or_404
from .models import Game, Rink
from django.views.generic import ListView

class GameListView(ListView):
    queryset = Game.gamelist.all()
    context_object_name = 'games'
    template_name = 'games/list.html'

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'games/game_detail.html', {'game': game})

def rink_detail(request, slug):
    rink = get_object_or_404(Rink, slug=slug)
    return render(request, 'rinks/rink_detail.html', {'rink': rink})