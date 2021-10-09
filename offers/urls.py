from django.urls import path
from .search import Search
from .confirm_pricing import ConfirmPricing
from .seatmap import Seatmap

urlpatterns = [
    path('search/', Search.as_view()),
    path('confirm-pricing/', ConfirmPricing.as_view()),
    path('seatmap/', Seatmap.as_view()),
]
