from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

from ckeditor_uploader.fields import RichTextUploadingField

from hhockeyUser.models import User

class GameListManager(models.Manager):
    def get_queryset(self):
        return super(GameListManager, self).get_queryset().filter(starttime__gte=timezone.now())

class Rink(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    picture = models.ImageField(blank=True, null=True)
    map = models.ImageField(blank=True, null=True)
    gmap_url = models.CharField(max_length=200, blank=True, null=True)
    skatesharpen = models.BooleanField()

    class Meta:
        ordering = ('name',)
        verbose_name = "Rink"

    def __str__(self):
        return self.name


class Game(models.Model):
    GAME_CHOICES = (
        ('PICKUP', 'Pick up Game'),
        ('MENS LEAGUE', 'Mens League'),
    )
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=15, choices=GAME_CHOICES, default='PICKUP')
    starttime = models.DateTimeField(default=timezone.now)
    cost = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    duration = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    rink = models.ForeignKey(Rink)
    recurring = models.BooleanField(default=False)

    class Meta:
        ordering = ('starttime',)
        verbose_name = "Game"

    def __str__(self):
        return self.name

    gamelist = GameListManager()
