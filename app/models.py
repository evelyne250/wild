from django.db import models

class Editor(models.Model):
    names = models.CharField(max_length =30)
