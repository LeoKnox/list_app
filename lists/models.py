from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    width = models.IntegerField()
    length = models.IntegerField()

def __str__(self):
    return self.title