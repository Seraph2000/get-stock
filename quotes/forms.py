from django import forms
from .models import Stock

# define and create form
class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["ticker"]