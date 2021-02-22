from django.urls import path
from . import views

urlpatterns = [
    path("news/", views.NewsCreateView.as_view()),
    path("news_details/", views.NewsDetailView.as_view()),
    path("news/<int:pk>/", views.NewsListView.as_view()),
    path("news/delete", views.NewsDeleteView.as_view()),
    path("event/", views.EventCreateView.as_view()),
    path("event/<int:pk>/", views.EventListView.as_view()),
    path("event_details/", views.EventDetailView.as_view()),
    path("person/", views.PersonsListView.as_view()),
    path("acredite/", views.AcreditationView.as_view()),
    path("gallery/", views.GalleryView.as_view()),

]
