from django.db import models

class Note(models.Model):
    name=models.CharField(max_length=200)
