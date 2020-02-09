from django.db import models

# Create your models here.
class MainDish(models.Model):
    name = models.TextField()

class SideDish(models.Model):
    name = models.TextField()
