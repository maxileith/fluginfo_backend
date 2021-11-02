from django.urls import path
from .search import Search
from .exact import Exact
from .seatmap import Seatmap

urlpatterns = [
    path('search/', Search.as_view()),
    path('exact/', Exact.as_view()),
    path('seatmap/', Seatmap.as_view()),
]
