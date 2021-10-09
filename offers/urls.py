from django.urls import path
from .search import Search
from .confirm_pricing import ConfirmPricing
from .seatmaps import Seatmaps

urlpatterns = [
    path('search/', Search.as_view()),
    path('confirm-pricing/', ConfirmPricing.as_view()),
    path('seatmaps/', Seatmaps.as_view()),
]
