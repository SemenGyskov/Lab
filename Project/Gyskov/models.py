from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

class Films(models.Model):
    name = models.CharField(max_length=50)
    date_out = models.DateField(blank=False)
    date_view = models.DateField(blank=False)
    actors = models.TextField()
    category = Category.name

