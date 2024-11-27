from .models import Articles
from django.forms import DateTimeInput, ModelForm, TextInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','announcement', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва статті'

            }),

            "announcement": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статті'

            }),

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статті'
            }),

            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публікації'
            })
        }