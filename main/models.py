from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    price = models.IntegerField()
    picture = models.URLField(max_length=100)
    description = models.TextField()