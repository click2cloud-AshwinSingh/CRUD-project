from django.db import models


# Create your models here.

class mymodel(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField(default=0)
    email = models.CharField(max_length=60)

    def __str__(self):
        return self.name
