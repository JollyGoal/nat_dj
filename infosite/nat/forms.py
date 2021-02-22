from django import forms
from .models import News, Acreditation


class NewsForm(forms.ModelForm):
    """ФОРМА НОВОСТЕЙ"""
    class Meta:
        model = News
        exclude = 'url', 'draft'

class AcreditationForm(forms.ModelForm):
    """ФОРМА НОВОСТЕЙ"""
    class Meta:
        model = Acreditation
        exclude = '__all__'
