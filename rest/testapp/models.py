from django.db import models

# Create your models here.
class Emp(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=50)
    esal = models.IntegerField()
    eadd = models.CharField(max_length=50)
    def __str__(self):
        return self.ename