from django.db import models

class TextImport(models.Model):
    textimportcsv = models.CharField( max_length=20000)

    def __str__(self):
        return self.textimportcsv

