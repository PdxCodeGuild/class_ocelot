from django.db import models

# Create your models here.
class LongUrl(models.Model):
    url = models.CharField( max_length=2000 )
    code = models.CharField(max_length=15)

    def __str__(self):
        return self.url_input_text
