from django import forms
from .models import Article
from .choices import *


class ArticleForm(forms.ModelForm):
    status = forms.ChoiceField(choices=STATUS_CHOICES, label="", initial='', widget=forms.Select(), required=True)
    location= forms.CharField(label='Deine Adresse', required=True)
    class Meta:
        model = Article
        fields = ('title', 'body', 'image', 'contact_email', 'contact_phone')#,'tags')

