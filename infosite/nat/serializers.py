from .models import Acreditation, Post, Gallery, Personal, Files, Contact, Text
from rest_framework import serializers

class PostListSerializer(serializers.ModelSerializer):
    """СПИСОК НОВОСТЕЙ"""

    class Meta:
        model = Post
        fields = 'title', 'date', 'category', 'url', 'id'

class PostDetailSerializer(serializers.ModelSerializer):
    """ПОДРОБНОСТИ НОВОСТЕЙ"""

    class Meta:
        model = Post
        exclude = 'draft',

class FileListSerializer(serializers.ModelSerializer):
    """ДОБАВЛЕНИЕ Файла"""

    class Meta:
        model = Files
        fields = '__all__'


class CreatePostSerializer(serializers.ModelSerializer):
    """ДОБАВЛЕНИЕ НОВОСТЕЙ"""

    class Meta:
        model = Post
        exclude = 'draft',


class AcreditationCreateSerializer(serializers.ModelSerializer):
    """АККРЕДИТАЦИЯ"""

    class Meta:
        model = Acreditation
        fields = ("__all__")

class ContactCreateSerializer(serializers.ModelSerializer):
    """АККРЕДИТАЦИЯ"""

    class Meta:
        model = Contact
        fields = ("__all__")



class GallerySerializer(serializers.ModelSerializer):
    """ГАЛЛЕРЕЯ"""

    class Meta:
        model = Gallery
        fields = 'image',


class PersonalListSerializer(serializers.ModelSerializer):
    """СПИСОК ПЕРСОНАЛА"""

    class Meta:
        model = Personal
        fields = '__all__'

class TextSerializer(serializers.ModelSerializer):
    """СЕРИАЛИЗАТОР КОММЕНТАРИЕВ"""
    class Meta:
        model = Text
        fields = '__all__'


