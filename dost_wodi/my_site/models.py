from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Zamovl(models.Model):
    chas_stvor=models.DateTimeField(auto_now_add=True)
    chas_dost=models.DateTimeField()
    stat=models.BooleanField(default=False)
    tel=PhoneNumberField(region="UA")
    adresa=models.CharField(max_length=255)
    vidpov=models.CharField(max_length=100)
    suma=models.DecimalField(max_digits=10, decimal_places=2)
    coment=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.chas_stvor