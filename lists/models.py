from django.db import models

class My_List(models.Model):
    item = models.CharField(max_length=50)
    qty = models.IntegerField()
    