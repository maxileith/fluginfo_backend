from django.urls import path
from .timings import Timings
from .exact import Exact
from .seatmap import Seatmap
from .search import Search

urlpatterns = [
    path('timings/', Timings.as_view()),
    path('search/', Search.as_view()),
    path('exact/', Exact.as_view()),
    path('seatmap/', Seatmap.as_view()),
]
