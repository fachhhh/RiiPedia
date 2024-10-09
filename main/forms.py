from django.forms import ModelForm
from main.models import Ecommerce
from django.utils.html import strip_tags

class EcommerceEntryForm(ModelForm):
    class Meta:
        model = Ecommerce
        fields = ["name", "price", "quantity", "description"]

    def clean_mood(self):
        mood = self.cleaned_data["mood"]
        return strip_tags(mood)

    def clean_feelings(self):
        feelings = self.cleaned_data["feelings"]
        return strip_tags(feelings)