from django import forms
from .models import Post, Acreditation


class PostForm(forms.ModelForm):
    """ФОРМА НОВОСТЕЙ"""
    class Meta:
        model = Post
        exclude = 'draft',

class AcreditationForm(forms.ModelForm):
    """ФОРМА НОВОСТЕЙ"""
    class Meta:
        model = Acreditation
        exclude = 'draft',
