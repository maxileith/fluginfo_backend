from django.urls import path
from .search import Search

urlpatterns = [
    path('search/', Search.as_view()),
]
