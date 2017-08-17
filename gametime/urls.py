from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.GameListView.as_view(), name='game_home'),
    url(r'^game/(?P<slug>[-\w]+)/$', views.game_detail, name='game_detail'),
    url(r'^rink/(?P<slug>[-\w]+)/$', views.rink_detail, name='rink_detail'),
]
