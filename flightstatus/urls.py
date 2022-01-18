from django.urls import path
from .timings import Timings

urlpatterns = [
    path('timings/', Timings.as_view()),
]
