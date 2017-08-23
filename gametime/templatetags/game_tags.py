from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe

from ..models import Game

register = template.Library()


@register.simple_tag
def get_user_in_game(user, id):
    gameList = Game.objects.get(id=int(id))
    userInGame = gameList.playerlist.filter(email=user)
    if userInGame:
        return True
    else:
        return False
