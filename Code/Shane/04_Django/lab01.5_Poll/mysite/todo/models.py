from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoItem(models.Model):
    todo_text = models.CharField(max_length=300)
    completed = models.BooleanField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.todo_text + ', completed = '+ str(self.completed)



