from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone

class TotoItem(models.Model):
    lyric = models.CharField(max_length=200)
    song = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return self.lyric + ' (' + self.song + ', ' + str(self.year) + ')'

class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    created = models.DateField(default=timezone.now)

    def str_id(self):
        return str(self.id)

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

    def toDictionary(self):
        return {'item_text': self.item_text,
                'due_date': self.due_date,
                'created': self.created,
                'urgency': self.urgency,
                'lyric': self.toto_item.lyric,
                'song': self.toto_item.song,
                'year': self.toto_item.year}


