from django import forms
from .models import CarAd, Brand

class CarAdForm(forms.ModelForm):
    new_brand = forms.CharField(
        max_length=50,
        required=False,
        label="Інша марка (якщо не в списку)"
    )

    class Meta:
        model = CarAd
        fields = ['brand', 'new_brand', 'model', 'year', 'price', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].queryset = Brand.objects.all()
        self.fields['brand'].required = False
        self.fields['brand'].empty_label = "Оберіть марку або введіть свою нижче"

    def clean(self):
        cleaned_data = super().clean()
        brand = cleaned_data.get('brand')
        new_brand = cleaned_data.get('new_brand')

        if not brand and not new_brand:
            raise forms.ValidationError("Потрібно обрати існуючу марку або ввести нову.")

        return cleaned_data

    def save(self, commit=True):
        brand = self.cleaned_data.get('brand')
        new_brand = self.cleaned_data.get('new_brand')

        if not brand and new_brand:
            brand, created = Brand.objects.get_or_create(name=new_brand)
        self.instance.brand = brand

        return super().save(commit)

class CarAdFilterForm(forms.Form):
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        required=False,
        empty_label="Всі марки",
        label="Марка"
    )
    year_min = forms.IntegerField(required=False, label='Рік від')
    year_max = forms.IntegerField(required=False, label='Рік до')
    price_min = forms.IntegerField(required=False, label='Ціна від')
    price_max = forms.IntegerField(required=False, label='Ціна до')
