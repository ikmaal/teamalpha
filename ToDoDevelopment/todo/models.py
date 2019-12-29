from django.db import models
from datetime import datetime

class TodoItem(models.Model):
    content = models.TextField()
    done = models.BooleanField(default=False)
    userID = models.IntegerField(default=1)
    timeStamp = models.DateTimeField(default=datetime.now)
