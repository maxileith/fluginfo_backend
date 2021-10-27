from django.urls import path
from .airports import AirportSearch, AirportDetails
from .countries import CountryFlag
from .airlines import AirlineLogo
from .flights import FlightRoute

urlpatterns = [
    path('airports/search/', AirportSearch.as_view()),
    path('airports/details/', AirportDetails.as_view()),
    path('countries/flag/', CountryFlag.as_view()),
    path('airlines/logo/', AirlineLogo.as_view()),
    path('flights/route/', FlightRoute.as_view()),
]
