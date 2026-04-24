from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    base_image = models.ImageField(upload_to='products/')
    
    # print area
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return self.name


class Design(models.Model):
    image = models.ImageField(upload_to='designs/')