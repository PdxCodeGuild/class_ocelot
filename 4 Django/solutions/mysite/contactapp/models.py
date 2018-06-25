from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    fav_fruit = models.CharField(max_length=200)
    fav_color = models.CharField(max_length=200)

    def __str__(self):
        return self.name



