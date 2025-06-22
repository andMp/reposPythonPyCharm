from django import forms

class AdForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=100)
    description = forms.CharField(label='Опис', widget=forms.Textarea)
    category = forms.ChoiceField(label='Категорія')

    def __init__(self, *args, **kwargs):
        categories = kwargs.pop('categories')
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = [(c.id, c.name) for c in categories]

class ResponseForm(forms.Form):
    name = forms.CharField(label='Им\'я', max_length=50)
    message = forms.CharField(label='Повідомлення', widget=forms.Textarea)
