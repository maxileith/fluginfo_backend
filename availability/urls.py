from django.urls import path
from .search import Search
from .exact import Exact

urlpatterns = [
    path('search/', Search.as_view()),
    path('exact/', Exact.as_view()),
]
