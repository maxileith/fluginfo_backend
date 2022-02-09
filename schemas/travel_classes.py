from rest_framework import fields
from drf_spectacular.utils import inline_serializer
from .price import price
from .stop import stop

travel_classes = fields.ChoiceField(
    choices=["ECONOMY", "FIRST", "BUSINESS", "PREMIUM_ECONOMY"], default="ECONOMY")
