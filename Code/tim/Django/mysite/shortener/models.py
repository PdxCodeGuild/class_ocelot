from django.db import models

class URL(models.Model):
    long_url = models.CharField(max_length=400)
    short_url = models.CharField(max_length=6)

    def __str__(self):
         return self.short_url
