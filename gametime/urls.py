from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.GameListView.as_view(), name='game_home'),
    url(r'^game/(?P<slug>[-\w]+)/$', views.game_detail, name='game_detail'),
    url(r'^rink/(?P<slug>[-\w]+)/$', views.rink_detail, name='rink_detail'),
    url(r'^mygames/$', views.ManageGameListView.as_view(), name='manage_game_list'),
    url(r'^create/$', views.GameCreateView.as_view(), name='game_create'),
    url(r'^(?P<pk>\d+)/edit/$', views.GameUpdateView.as_view(), name='game_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.GameDeleteView.as_view(), name='game_delete'),
    url(r'^(?P<pk>\d+)/join/$', views.game_join, name='game_join'),
    url(r'^(?P<pk>\d+)/leave/$', views.game_leave, name='game_leave'),

]
