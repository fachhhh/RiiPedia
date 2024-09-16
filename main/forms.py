from django.forms import ModelForm
from main.models import Ecommerce

class EcommerceEntryForm(ModelForm):
    class Meta:
        model = Ecommerce
        fields = ["name", "price", "quantity", "description"]