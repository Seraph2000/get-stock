from django.db import models

# Create your models here.
class Stock(models.Model):
    # define our database - what do we want to save
    ticker = models.CharField(max_length=10)
    
    def __str__(self):
        # for the admin area
        return self.ticker
