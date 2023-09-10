from django.db import models


# Create your models here.
class Inquiry(models.Model):
    Entername = models.CharField(max_length=50)
    Company = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact = models.BigIntegerField()
    Message = models.CharField(max_length=50)
    Link = models.CharField(max_length=50)

# def __str__(self):
#         return self.entername

