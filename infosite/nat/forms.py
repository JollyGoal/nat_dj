from django import forms
from .models import Post, Acreditation, Contact


class PostForm(forms.ModelForm):
    """ФОРМА НОВОСТЕЙ"""
    class Meta:
        model = Post
        exclude = 'draft',

class AcreditationForm(forms.ModelForm):
    """ФОРМА АККРЕДИТАЦИИ"""
    class Meta:
        model = Acreditation
        fields = '__all__'

class ContactForm(forms.ModelForm):
    """ФОРМА КОНТАКТОВ"""
    class Meta:
        model = Contact
        exclude = 'date'
