from django.db import models


# Create the Game model class, a subclass of django.db.models.Model
class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, default='')
    release_date = models.DateTimeField()
    game_category = models.CharField(max_length=200, blank=True, default='')
    played = models.BooleanField(default=False)

    # Meta is an inner class with a tuple-type variable ordering
    # set it to the games by name
    class Meta:
        ordering = ('name',)
