from django.db import models
from django.db.models.base import Model

class About(models.Model):
    title       = models.CharField(max_length=100 , blank=True)
    text_body   = models.TextField(blank=True)
    def __str__(self):
        return self.title