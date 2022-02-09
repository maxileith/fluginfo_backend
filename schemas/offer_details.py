import rest_framework.serializers as fields
from drf_spectacular.utils import inline_serializer
from .price import price
from .stop import stop
from .travel_classes import travel_classes
from copy import copy

segment = inline_serializer(name="Segment", fields={
    "id": fields.IntegerField(help_text="e.g. 1"),
    "departure": copy(stop),
    "arrival": copy(stop),
    "flightNumber": fields.CharField(help_text="e.g. LH438"),
    "carrierCode": fields.CharField(help_text="e.g. LH"),
    "carrier": fields.CharField(help_text="e.g. LUFTHANSA"),
    "duration": fields.IntegerField(help_text="e.g. 670"),
    "aircraft": fields.CharField(help_text="e.g. AIRBUS A330-300"),
    "cabin": copy(travel_classes),
    "classId": fields.CharField(help_text="e.g. Y"),
})

itinerary = inline_serializer(name="Itinerary (Details)", fields={
    "duration": fields.IntegerField(help_text="e.g. 670"),
    "segments": fields.ListField(child=copy(segment)),
})

offer_details_response_schema = inline_serializer(name="OfferDetailsResponse", fields={
    "price": copy(price),
    "itineraries": fields.ListField(child=copy(itinerary)),
})
