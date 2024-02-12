from django.db import models


# Create your models here.
class post(models.Model):
    first_name = models.CharField(max_length=100)
    user_image = models.ImageField()
