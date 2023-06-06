from django.db import models


# Create your models here.
class Notes(models.Model):
    id = models.BigAutoField(primary_key=True)
    owner = models.IntegerField()
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=5000)
