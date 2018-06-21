from django.db import models

from django.utils import timezone

class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    date_completed = models.DateTimeField(null=True, blank=True)

    def completed(self):
        return self.date_completed is not None

    def pretty_created_date(self):
        return self.date_created.strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return self.text

