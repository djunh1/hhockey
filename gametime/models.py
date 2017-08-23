from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField

from hhockeyUser.models import User


class GameListManager(models.Manager):
    def get_queryset(self):
        return super(GameListManager, self).get_queryset().filter(starttime__gte=timezone.now())


class RecurringListManager(models.Manager):
    def get_queryset(self):
        return super(RecurringListManager, self).get_queryset().filter()


class Rink(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    picture = models.ImageField(blank=True, null=True)
    map = models.ImageField(blank=True, null=True)
    gmap_url = models.CharField(max_length=200, blank=True, null=True)
    skatesharpen = models.BooleanField()
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "Rink"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game:rink_detail', args=[self.slug])

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
    RECURRENCE_CHOICES = (
        (0, 'Once'),
        (1, 'Daily'),
        (7, 'Weekly'),
        (14, 'Biweekly')
    )

    owner = models.ForeignKey(User, related_name='games_created')
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=15, choices=GAME_CHOICES, default='PICKUP')
    slug = models.SlugField(max_length=50, unique=True)
    status = models.CharField(max_length=15, choices=REPORT_STATUS, default='ON')
    starttime = models.DateTimeField(default=timezone.now)
    frequency = models.IntegerField(choices=RECURRENCE_CHOICES)
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

    def players_count(self):
        return self.playerlist.count()

    def get_absolute_url(self):
        return reverse('game:game_detail',
                       args=[self.slug])

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Game.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        '''
        Auto generate a slug, and autoamtically put creator in game.
        TODO make sure if they leave that there isn't a bug
        '''
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()
        self.playerlist.add(self.owner)

    objects = models.Manager()
    gamelist = GameListManager()