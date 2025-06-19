class Vidguc:
    def __init__(self, vidguc):
        name = forms.CharField(label='Имя', max_length=50)
        message = forms.CharField(label='Сообщение', widget=forms.Textarea)