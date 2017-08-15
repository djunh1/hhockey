from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.GameListView.as_view(), name='game_list'),
]
