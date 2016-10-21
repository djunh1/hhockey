from django.db import models
from django.conf import settings


LEAGUE_CHOICES = (
    ('HOUSE LEAGUE', 'House League'),
    ('TRAVEL LEAGUE', 'Travel League'),
    ('JUNIORS', 'Juniors'),
    ('COLLEGE', 'College'),
    ('MAJOR JUNIORS', 'Major Juniors'),
    ('PROFESSIONAL', 'Professional'),
)

POSITION_CHOICES = (
    ('WING', 'Wing'),
    ('CENTER', 'Center'),
    ('DEFENSE', 'Defense'),
)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    birth_date = models.DateField(null=True, blank=True)
    league = models.CharField(max_length=15, choices=LEAGUE_CHOICES, blank=True)
    position = models.CharField(max_length=8, choices=POSITION_CHOICES, blank=True)

    def __str__(self):
        return'Profile for user {}'.format(self.user.username)