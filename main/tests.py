from django.test import TestCase
from .models import Ecommerce

class EcommerceModelTest(TestCase):
    def setUp(self):
        # Set up a few instances of the Ecommerce model
        Ecommerce.objects.create(name="Product A", price=100, quantity=60, description="Description of Product A")
        Ecommerce.objects.create(name="Product B", price=150, quantity=30, description="Description of Product B")

    def test_ecommerce_str(self):
        # Test that the string representation is correct
        product = Ecommerce.objects.get(name="Product A")
        self.assertEqual(str(product), "Product A")

    def test_is_quantity_more_than_50_true(self):
        # Test if is_quantity_more_than_50 is True when quantity is more than 50
        product = Ecommerce.objects.get(name="Product A")
        self.assertTrue(product.is_quantity_more_than_50)

    def test_is_quantity_more_than_50_false(self):
        # Test if is_quantity_more_than_50 is False when quantity is 50 or less
        product = Ecommerce.objects.get(name="Product B")
        self.assertFalse(product.is_quantity_more_than_50)
