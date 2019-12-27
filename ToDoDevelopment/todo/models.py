from django.db import models
from datetime import datetime

class TodoItem(models.Model):
    content = models.TextField()
    delete = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    userID = models.IntegerField(default=1)
