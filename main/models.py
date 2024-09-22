from django.db import models
from django.contrib.auth.models import User
import uuid

class Ecommerce(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    price = models.IntegerField() # harga maks adalah dalam satuan miliar dengan 3 decimal
    quantity = models.IntegerField()
    description = models.TextField()

    @property
    def is_quantity_more_than_50(self):
        return self.quantity > 50