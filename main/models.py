from django.db import models
import uuid

class Ecommerce(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=13, decimal_places=3) # harga maks adalah dalam satuan miliar dengan 3 decimal
    quantity = models.IntegerField()
    description = models.TextField()

    @property
    def is_quantity_more_than_50(self):
        return self.quantity > 50