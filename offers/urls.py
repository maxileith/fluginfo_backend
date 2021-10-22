from django.urls import path
from .search import Search
from .seatmaps import Seatmaps
from .details import Details

urlpatterns = [
    path('search/', Search.as_view()),
    path('seatmaps/', Seatmaps.as_view()),
    path('details/', Details.as_view()),
]
