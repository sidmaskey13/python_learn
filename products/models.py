from django.db import models

# Create your models here.
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2,max_digits=100000)
    summary = models.TextField(default="This is great product")
    featured = models.BooleanField(null=True, default=False)

    def get_absolute_url(self):
        return reverse("products", kwargs={"id": self.id})
    
    
