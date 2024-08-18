from django.db import models

class Todo(models.Model):
    todo_type = models.CharField(max_length=200)
    text = models.TextField()

