from django.db import models

# Create your models here.


class Area(models.Model):
    acname = models.CharField(max_length=20)
    aename = models.CharField(max_length=50)
    methodnum = models.IntegerField()
    adescription = models.CharField(max_length=1000)
    ainfolink = models.CharField(max_length=50)

    def __str__(self):
        return self.acname


class Mehtods(models.Model):
    mcname = models.CharField(max_length=20)
    mename = models.CharField(max_length=50)
    mtype = models.ForeignKey('Area', on_delete=models.DO_NOTHING)
    mdescription = models.CharField(max_length=1000)
    minfolink = models.CharField(max_length=50)
    myear = models.IntegerField(default=0)
    mpersons = models.CharField(max_length=100, default=None)
    mhot = models.IntegerField(default=0)

    def __str__(self):
        return self.mcname


class Link(models.Model):
    url = models.CharField(max_length=100)
    source = models.CharField(max_length=20)
    method = models.ForeignKey("Mehtods", on_delete=models.DO_NOTHING)
    linkhot = models.IntegerField(default=0)