from django.urls import path
from .search import Search
from .seatmap import Seatmap
from .details import Details

urlpatterns = [
    path('search/', Search.as_view()),
    path('seatmaps/', Seatmap.as_view()),
    path('details/', Details.as_view()),
]
