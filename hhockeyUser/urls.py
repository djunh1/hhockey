from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^games_created/$', views.GameCreatedList.as_view(), name='game_created_list'),
    url(r'^games_joined/$', views.GameJoinedList.as_view(), name='game_joined_list'),

]