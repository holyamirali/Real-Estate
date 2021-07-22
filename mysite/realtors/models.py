from django.db import models

class Realtor(models.Model):
    name        = models.CharField(max_length=30)
    phone       = models.CharField(max_length=15)
    address     = models.TextField(blank=True)
    email       = models.CharField(max_length=50)
    facebook    = models.CharField(max_length=30 , blank=True)
    photo_main  = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name