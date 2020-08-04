from django.db import models

# Create your models here.
class Songs(models.Model):
    title= models.CharField(max_length=50, null=False)
    artist = models.CharField(max_length=50, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)