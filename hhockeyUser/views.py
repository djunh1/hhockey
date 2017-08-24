from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic

from braces.views import LoginRequiredMixin

from gametime.models import Game
from hhockeyUser.models import User

from .mixins import PageTitleMixin


class GameCreatedList(PageTitleMixin, ListView):
    def get_queryset(self):
        return Game.gamelist.filter(owner=self.request.user)
    context_object_name = 'games'
    template_name = 'games/created_list.html'
    active_tab = 'gametime'


class GameJoinedList(PageTitleMixin, ListView):
    def get_queryset(self):
        return Game.objects.filter(playerlist__in = [self.request.user])
    context_object_name = 'games'
    template_name = 'games/joined_list.html'
    active_tab = 'gametime'
