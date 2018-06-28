from django.db import models

from django.contrib.auth.models import User


class TodoList(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# @login_required
# def list_todolists(request):
#     todo_lists = request.user.todolist_set.all()
#
