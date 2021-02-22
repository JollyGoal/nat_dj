from .models import Acreditation, News, Event, Gallery, Personal
from rest_framework import serializers

class NewsListSerializer(serializers.ModelSerializer):
    """СПИСОК НОВОСТЕЙ"""

    class Meta:
        model = News
        fields = ("id", "title", "date", "image", "url")

class NewsDetailSerializer(serializers.ModelSerializer):
    """ПОЛНЫЕ ДЕТАЛИ НОВОСТЕЙ"""

    class Meta:
        model = News
        exclude = ("draft",)

class CreateNewsSerializer(serializers.ModelSerializer):
    """ДОБАВЛЕНИЕ НОВОСТЕЙ"""

    class Meta:
        model = News
        exlude = 'url', 'draft'

class EventListSerializer(serializers.ModelSerializer):
    """СПИСОК МЕРОПРИЯТИЙ"""

    class Meta:
        model = Event
        fields = ("id", "title", "date", "image", "url")

class EventDetailSerializer(serializers.ModelSerializer):
    """ДЕТАЛИ МЕРОПРИЯТИЙ"""

    class Meta:
        model = Event
        fields = ("__all__")

class EventCreateSerializer(serializers.ModelSerializer):
    """ДОБАВЛЕНИЕ МЕРОПРИЯТИЙ"""

    class Meta:
        model = Event
        exlude = 'url', 'draft'


class AcreditationCreateSerializer(serializers.ModelSerializer):
    """АККРЕДИТАЦИЯ"""

    class Meta:
        model = Acreditation
        fields = ("__all__")



class GallerySerializer(serializers.ModelSerializer):
    """ГАЛЛЕРЕЯ"""

    class Meta:
        model = Gallery
        fields = 'image'

class PersonalListSerializer(serializers.ModelSerializer):
    """СПИСОК ПЕРСОНАЛА"""

    class Meta:
        model = Personal
        exlude = '__all__'


