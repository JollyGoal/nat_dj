from rest_framework.generics import ListAPIView
from .models import News, Gallery, Personal, Event, Acreditation
from .serializers import (
    NewsListSerializer,
    NewsDetailSerializer,
    GallerySerializer,
    CreateNewsSerializer,
    PersonalListSerializer,
    EventListSerializer,
    EventDetailSerializer,
    AcreditationCreateSerializer,
    EventCreateSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.mixins import LoginRequiredMixin

class AcreditationView(LoginRequiredMixin, generics.CreateAPIView):
    """АККРЕДИТАЦИЯ СМИ"""
    serializer_class = AcreditationCreateSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class NewsListView(ListAPIView):
    """вывод список новостей"""
    queryset = News.objects.filter(draft=False)
    serializer_class = NewsListSerializer
    pagination_class = LargeResultsSetPagination

class NewsDetailView(APIView):

    def get(self, request, pk):
        news = News.objects.get(id=pk, draft=False)
        serializer = NewsDetailSerializer(news)
        news_shots = Gallery.objects.filter(news__id=pk)
        ser_shots = GallerySerializer(news_shots, many=True)
        return Response({'news': serializer.data, 'shots': ser_shots.data})

    def post(self, request, pk):
        news = News.objects.get(id=pk, draft=False)
        serializer = NewsDetailSerializer(news)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewsCreateView(LoginRequiredMixin, generics.CreateAPIView):
    """ДОБАВЛЕНИЕ НОВОСТЕЙ"""
    serializer_class = CreateNewsSerializer
    permission_classes = [permissions.IsAdminUser]

class NewsDeleteView(generics.DestroyAPIView):
    """УДАЛЕНИЕ ОТЗЫВА"""
    queryset = News.objects.all()
    permission_classes = [permissions.IsAdminUser]

class PersonsListView(generics.ListAPIView):
    """ВЫВОД СПИСКА ПЕРСОН"""
    queryset = Personal.objects.all()
    serializer_class = PersonalListSerializer
    pagination_class = LargeResultsSetPagination

class GalleryView(generics.ListAPIView):
    """ВЫВОД СПИСКА ПЕРСОН"""
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    pagination_class = LargeResultsSetPagination


class EventListView(ListAPIView):
    """вывод список новостей"""
    queryset = Event.objects.filter(draft=False)
    serializer_class = EventListSerializer
    pagination_class = LargeResultsSetPagination

class EventCreateView(LoginRequiredMixin, generics.CreateAPIView):
    """ДОБАВЛЕНИЕ МЕРОПРИЯТИЙ"""
    serializer_class = EventCreateSerializer
    permission_classes = [permissions.IsAdminUser]

class EventDetailView(APIView):

    def get(self, request, pk):
        event = Event.objects.get(id=pk, draft=False)
        serializer = EventDetailSerializer(event)
        news_shots = Gallery.objects.filter(event__id=pk)
        ser_shots = GallerySerializer(news_shots, many=True)
        return Response({'event': serializer.data, 'shots': ser_shots.data})

    def post(self, request, pk):
        event = Event.objects.get(id=pk, draft=False)
        serializer = EventDetailSerializer(event)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)