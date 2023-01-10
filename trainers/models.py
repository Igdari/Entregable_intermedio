from django.db import models

class Trainers(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    free = models.BooleanField(default=True)

    def __str__(self):
        return self.name
