from django.urls import path
from . import views

urlpatterns = [
    path("category/", views.CategoryListView.as_view()),
    path("post/<int:pk>", views.PostDetailView.as_view()),
    path("post/", views.PostListView.as_view()),
    path("person/", views.PersonsListView.as_view()),
    path("acredite/", views.AcreditationView.as_view()),
    path("gallery/", views.GalleryView.as_view()),
    path("files/", views.FilesListView.as_view()),
    path("contact/", views.ContactView.as_view()),
    path("sponsor/", views.SponsorView.as_view()),
]
