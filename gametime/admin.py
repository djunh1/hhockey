from django.contrib import admin
from .models import Rink, Game, Comment, CustomPlayerList

'''
class RinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'post_code', 'skatesharpen')
    search_fields = ('name', 'post_code')
    list_filter = ('name', 'address', 'post_code', 'skatesharpen')
    ordering = ['name', 'post_code']
    prepopulated_fields = {'slug': ('name','post_code')}

admin.site.register(Rink, RinkAdmin)

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'starttime', 'cost', 'duration', 'rink')
    list_filter = ('name', 'starttime', 'cost')
    search_fields = ('name', 'starttime')
    ordering = ['starttime',]
    prepopulated_fields = {'slug': ('name',) }
admin.site.register(Game, GameAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('user', 'body')

admin.site.register(Comment, CommentAdmin)

class CustomListAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    list_filter = ('name', 'created')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',) }

admin.site.register(CustomPlayerList, CustomListAdmin)

'''