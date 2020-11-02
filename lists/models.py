from django.db import models

class My_List(models.Model):
    item = models.CharField(max_length=50)
    qty = models.IntegerField()
    subsititute = models.CharField(max_length=50, null=True)
    urgent = models.BooleanField()

class Sub_List(models.Model):
    recipes = models.CharField(max_length=50)
    list = models.ForeignKey(My_List, on_delete=models.CASCADE)

class Store_List(models.Model):
    store_name = models.CharField(max_length = 50)
    lists = models.ManyToManyField(My_List)

def __str__(self):
    return self.title