from django.db import models
from django.contrib.auth import authenticate, login

from django.utils import timezone

import datetime


# Create your models here.

class TodoItem(models.Model):
    todo_text = models.CharField(max_length=300)
    completed = models.BooleanField()

    def __str__(self):
        return self.todo_text + ', completed = '+ str(self.completed)



