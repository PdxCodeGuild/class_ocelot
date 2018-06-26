from django.db import models

# only 1 model, because only url and code; no need for more.
class UrlList(models.Model):
    url = models.CharField( max_length=2000)
    code = models.CharField(max_length=15)

    def __str__(self):
        return self.url_input_text
