from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    #

    def __str__(self):
        return'Profile for user {}'.format(self.user.username)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class MemberProfile(models.Model):
    pass
    '''
    (1) Start date of an individual stick Membership.
    (2) Expiration Date - whenever start date of membership + 365, when does membership reset?
    (3) Stick info -  tuple with flex, curve, when purchased.

    def cancel(self, last purchase stick, value, current date, monthly fee):
        pass
        How much is left to pay on the amortization schedule of 1 hockey stick.  This would be only for the
        last stick ( only most recent stick)
        return(dollar value)

    def hockeyStickReplacementNumber(self):
        pass
        How many replacement sticks in the last 365 days.  If =< 2, replacement stick fee is 35.  >2, 100.
        return dictionary ['35$': 2 , '$100' : 1]


    '''