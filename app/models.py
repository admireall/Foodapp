from django.db import models

# Create your models here.
class movies(models.Model):

    def __str__(self):
        return self.name # TODO
    name=models.CharField(max_length=200)
    rating=models.FloatField()
