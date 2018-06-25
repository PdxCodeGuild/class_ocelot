
from django.utils import timezone
from django.db import models

class TotoItem(models.Model):
    lyric = models.CharField(max_length=200)
    song = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return self.lyric + ' (' + self.song + ', ' + str(self.year) + ')'

class TodoList(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class TodoItem(models.Model):
    item_text = models.CharField(max_length=200)
    due_date = models.DateTimeField('due date')
    urgency = models.CharField(max_length=20, default='Meh')
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    toto_item = models.ForeignKey(TotoItem, on_delete=models.CASCADE)
    created = models.DateField(default=timezone.now)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item_text
