from django.db import models

# Create your models here.
class BookList(models.Model):
    title = models.TextField(default=None)
    author = models.TextField(default=None)
    year = models.PositiveIntegerField(default=None)
