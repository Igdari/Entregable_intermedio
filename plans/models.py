from django.db import models

class Plans(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField()
    
    def __str__(self):
        return self.name