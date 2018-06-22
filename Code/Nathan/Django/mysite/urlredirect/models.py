from django.db import models


# Create your models here.




class Shortener(models.Model):
    code = models.CharField(max_length=25)
    urls = models.CharField(max_length=2083)

    def __str__(self):
        return self.code + ' ' + self.urls

    # def __str__(self):
    #     return self.urls
