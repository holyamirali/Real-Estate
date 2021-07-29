from django.db import models
from datetime import datetime

from django.db.models.fields import NullBooleanField
from realtors.models import Realtor

class Listings(models.Model):
    title           = models.CharField(max_length=150 , blank=True)
    realtor         = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, blank=True, null=True)
    price           = models.IntegerField(null=True)
    #type            = models.CharField(max_length=15 , blank=True)
    address         = models.TextField(blank=True)
    bathroom        = models.IntegerField(default=1)
    bedroom         = models.IntegerField(default=1)
    garages         = models.IntegerField(default=1)
    floors          = models.IntegerField(default=1)
    infrastructure  = models.CharField(max_length=100)
    details         = models.TextField()
    is_published    = models.BooleanField(default=True)
    list_data       = models.DateTimeField(blank=True, default=datetime.now)
    photo_main      = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_1         = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_2         = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.title
