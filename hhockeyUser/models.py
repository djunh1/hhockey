from django.db import models
from oscar.apps.customer.abstract_models import AbstractUser as CoreAbstractUser

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



class User(CoreAbstractUser):
    username = models.CharField(max_length=25, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    league = models.CharField(max_length=15, choices=LEAGUE_CHOICES, blank=True)
    position = models.CharField(max_length=8, choices=POSITION_CHOICES, blank=True)
