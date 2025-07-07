from django.db import models

# Create your models here.
class Zavd(models.Model):
    name=models.CharField(max_length=50)
    stan=models.BooleanField(default=False)
    description=models.TextField(blank=True)
    date=models.DateTimeField()

    def __str__(self):
        return self.name