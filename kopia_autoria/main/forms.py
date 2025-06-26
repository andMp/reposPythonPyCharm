from django import forms
from .models import CarAd

class CarAdForm(forms.ModelForm):
    class Meta:
        model = CarAd
        fields = ['brand', 'model', 'year', 'price', 'description']

class CarAdFilterForm(forms.Form):
    brand = forms.ChoiceField(choices=[('', 'Всі марки')] + CarAd.BRAND_CHOICES, required=False)
    year_min = forms.IntegerField(required=False, label='Рік від')
    year_max = forms.IntegerField(required=False, label='Рік до')
    price_min = forms.IntegerField(required=False, label='Ціна від')
    price_max = forms.IntegerField(required=False, label='Ціна до')

