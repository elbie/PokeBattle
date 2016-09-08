from django.db import models

class PokemonType(models.Model):
    type = models.TextField()

class Attack(models.Model):
    attack = models.ForeignKey('PokemonType')
    defense = models.ForeignKey('PokemonType')
    NO_EFFECT = 'NE'
    NOT_VERY_EFFECTIVE = 'NV'
    NORMAL = 'NO'
    SUPER_EFFECTIVE = 'SE'
    effect = models.IntegerField(default=NORMAL)
