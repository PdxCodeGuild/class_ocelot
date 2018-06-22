from django.db import models


# Create your models here.

class ShortUrl(models.Model):
    short_url = models.CharField(max_length=50)
    long_url = models.CharField(max_length=3000)

    def __str__(self):
        return self.short_url
