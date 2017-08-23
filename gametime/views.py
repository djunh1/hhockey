from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from hhockeyUser.models import User
from .models import Game, Rink


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)


class OwnerGameMixin(OwnerMixin, LoginRequiredMixin):
    model = Game


class OwnerGameEditMixin(OwnerGameMixin, OwnerEditMixin):
    fields = ['name', 'type', 'starttime', 'frequency', 'rink']
    success_url = reverse_lazy('game:manage_game_list')
    template_name = 'games/manage/form.html'


class ManageGameListView(OwnerGameMixin, ListView):
    template_name = 'games/manage/list.html'


class GameCreateView(PermissionRequiredMixin,OwnerGameEditMixin, CreateView):
    permission_required = 'gametime.add_game'



class GameUpdateView(PermissionRequiredMixin, OwnerGameEditMixin, UpdateView):
    template_name = 'games/manage/form.html'
    permission_required = 'gametime.change_game'


class GameDeleteView(PermissionRequiredMixin, OwnerGameMixin, DeleteView):
    template_name = 'games/manage/delete.html'
    success_url = reverse_lazy('game:manage_game_list')
    permission_required = 'gametime.delete_game'


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

class ManageGameListView(ListView):
    model = Game
    template_name = 'games/manage/user_list_games.html'

    def get_queryset(self):
        qs = super(ManageGameListView, self).get_queryset()
        return qs.filter(owner=self.request.user)

@login_required
def game_join(request, pk):
    game = get_object_or_404(Game, id=pk)
    userJoined = False

    try:
        playerUser = request.user
    except Exception:
            userJoined= 'No user by this name'
            return render(request, 'games/player_join.html', {'game': game, 'userJoined': userJoined})

    if playerUser in game.playerlist.all():
        userJoined = True
        userJoined = ' This user is already in the game'
        return render(request, 'games/player_join.html', {'game': game, 'userJoined': userJoined})
    else:
        game.playerlist.add(playerUser)
        userJoined = True
        userJoined = ' Welcome to the game'
        return render(request, 'games/player_join.html', {'game': game, 'userJoined': userJoined})

@login_required
def game_leave(request, pk):
    game = get_object_or_404(Game, id=pk)
    try:
        playerUser = request.user
    except Exception:
            userJoined= 'No user by this name'
            return render(request, 'games/player_join.html', {'game': game, 'userJoined': userJoined})
    game.playerlist.remove(playerUser)
    return render(request, 'games/manage/remove_player.html', {'game': game})
