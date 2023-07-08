from distutils.command.upload import upload
from tabnanny import verbose
from unicodedata import name
from django.db import models

class ImageAdverts(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')


    class Meta:
        verbose_name_plural = "Images Advertisements"

    def __str__(self):
        return self.name


