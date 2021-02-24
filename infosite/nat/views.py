from rest_framework.generics import ListAPIView
from .models import Gallery, Personal, Post, Sponsor, Files, Text, Category
from .serializers import (
    PostListSerializer,
    GallerySerializer,
    CreatePostSerializer,
    PersonalListSerializer,
    AcreditationCreateSerializer,
    FileListSerializer,
    PostDetailSerializer,
    ContactCreateSerializer,
    TextSerializer,
    SponsorSerializer,
    CategoryListSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics, filters
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.mixins import LoginRequiredMixin


class AcreditationView(LoginRequiredMixin, generics.CreateAPIView):
    """АККРЕДИТАЦИЯ СМИ"""
    serializer_class = AcreditationCreateSerializer

class ContactView(LoginRequiredMixin, generics.CreateAPIView):
    """КОНТАКТ С НАМИ"""
    serializer_class = ContactCreateSerializer

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class PostListView(ListAPIView):
    """вывод список новостей"""
    queryset = Post.objects.filter(draft=False)
    serializer_class = PostListSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'category__name']


class CategoryListView(ListAPIView):
    """вывод список категорий"""
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    pagination_class = LargeResultsSetPagination


class PostDetailView(APIView):

    def get(self, request, pk):
        post = Post.objects.get(id=pk, draft=False)
        serializer = PostDetailSerializer(post)
        file = Files.objects.filter(documents__id=pk)
        files = FileListSerializer(file, many=True)
        sponsor = Sponsor.objects.filter(logo__id=pk)
        sponsors = SponsorSerializer(sponsor, many=True)
        text = Text.objects.filter(add__id=pk)
        texts = TextSerializer(text, many=True)
        post_shots = Gallery.objects.filter(gallery__id=pk)
        ser_shots = GallerySerializer(post_shots, many=True)
        pers_shots = Personal.objects.filter(personal__id=pk)
        sen_shots = PersonalListSerializer(pers_shots, many=True)
        return Response({'post': serializer.data, 'gallery': ser_shots.data,
                         'personal': sen_shots.data, 'texts': texts.data,
                         'files': files.data,
                         'sponsors': sponsors.data})

    def post(self, request, pk):
        news = Post.objects.get(id=pk, draft=False)
        serializer = PostListSerializer(news)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class PostCreateView(LoginRequiredMixin, generics.CreateAPIView):
    """ДОБАВЛЕНИЕ НОВОСТЕЙ"""
    serializer_class = CreatePostSerializer
    # permission_classes = [permissions.IsAdminUser]


class PersonsListView(generics.ListAPIView):
    """ВЫВОД СПИСКА ПЕРСОН"""
    queryset = Personal.objects.all()
    serializer_class = PersonalListSerializer
    pagination_class = LargeResultsSetPagination


class GalleryView(generics.ListAPIView):
    """ВЫВОД СПИСКА ГАЛЛЕРЕИ"""
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    pagination_class = LargeResultsSetPagination


class FilesListView(generics.ListAPIView):
    """ВЫВОД СПИСКА ФАЙЛОВ"""
    queryset = Files.objects.all()
    serializer_class = FileListSerializer
    pagination_class = LargeResultsSetPagination

# class TextView(generics.ListAPIView):
#     """ВЫВОД СПИСКА ТЕМ"""
#     queryset = Text.objects.all()
#     serializer_class = TextSerializer
#     pagination_class = LargeResultsSetPagination
