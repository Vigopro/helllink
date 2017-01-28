from django.db import models

# Create your models here.
from shortener.models import ShortURL

class ClickCounterManager(models.Manager):
    def create_event(self, shortInstance):
        if isinstance(shortInstance, ShortURL):
            obj, created = self.get_or_create(short_url=shortInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickCounter(models.Model):
    short_url = models.OneToOneField(ShortURL)
    count     = models.IntegerField(default=0)
    update    = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickCounterManager()

    def __str__(self):
        return "{i}".format(i=self.count)
