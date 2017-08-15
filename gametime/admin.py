from django.contrib import admin
from .models import Rink, Game, RecurringGame


class RinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'post_code', 'skatesharpen')
    search_fields = ('name', 'post_code')
    list_filter = ('name', 'address', 'post_code', 'skatesharpen')
    ordering = ['name', 'post_code']

admin.site.register(Rink, RinkAdmin)

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'starttime', 'cost', 'duration', 'rink')
    list_filter = ('name', 'starttime', 'cost')
    search_fields = ('name', 'starttime')
    ordering = ['starttime',]
admin.site.register(Game, GameAdmin)

class RecGameAdmin(admin.ModelAdmin):
    list_display = ('recgame', 'day')
    list_filter= ('recgame', 'day')
    search_fields = ('recgame', 'day')
    ordering = ['day']
admin.site.register(RecurringGame, RecGameAdmin)