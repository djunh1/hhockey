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

    objects = models.Manager()

class Game(models.Model):
    GAME_CHOICES = (
        ('PICKUP', 'Pick up Game'),
        ('MENS LEAGUE', 'Mens League'),
    )
    REPORT_STATUS = (
        ('ON', 'On'),
        ('MAYBE', 'Maybe'),
        ('No', 'No'),
    )

    owner = models.ForeignKey(User, related_name='games_created')
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=15, choices=GAME_CHOICES, default='PICKUP')
    status = models.CharField(max_length=15, choices=REPORT_STATUS, default='ON')
    starttime = models.DateTimeField(default=timezone.now)
    cost = models.DecimalField(max_digits=5, decimal_places=2, default='0.0')
    duration = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    rink = models.ForeignKey(Rink)
    recurring = models.BooleanField(default=False)
    playerlist = models.ManyToManyField(User, blank=True, null=True)

    class Meta:
        ordering = ('starttime',)
        verbose_name = "Game"

    def __str__(self):
        return self.name

    objects = models.Manager()
    gamelist = GameListManager()

class RecurringGame(models.Model):
    DAY_CHOICES = (
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
        ('SATURDAY', 'Saturday'),
        ('SUNDAY', 'Sunday'),

    )
    recgame = models.ForeignKey(Game, related_name='recurring_game')
    day = models.CharField(max_length=15, choices=DAY_CHOICES)

    objects = models.Manager()