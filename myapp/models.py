from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import datetime

# Create your models here.

class NotesGroup(models.Model):
    title = models.CharField(null=False, max_length=50)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.title


class Note(models.Model):
    title = models.CharField(null=False, max_length=50)
    date = models.DateTimeField(default=datetime.now())
    content = models.TextField()
    notes_group = models.ForeignKey(NotesGroup, on_delete=models.CASCADE)
    favourite = models.BooleanField(default=False)
    public = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    