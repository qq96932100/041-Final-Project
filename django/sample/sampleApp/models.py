from django.db import models

# Create your models here.

class Sample(models.Model):
    sName = models.CharField(max_length=20,null=False)
    sSex = models.CharField(max_length=2,default='M',null=False)
    sPhone = models.CharField(max_length=50,blank=True,default='')

    def __str__(self):
        return self.sName