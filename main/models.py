from django.db import models
import uuid

class Ecommerce(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()

    @property
    def is_quantity_more_than_50(self):
        return self.quantity > 50