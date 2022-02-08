import rest_framework.serializers as fields
from drf_spectacular.utils import inline_serializer
from .price import price
from .stop import stop
from .travel_classes import travel_classes
from copy import copy

segment = inline_serializer(name="Segment", fields={
    "id": fields.IntegerField(default=1),
    "departure": copy(stop),
    "arrival": copy(stop),
    "flightNumber": fields.CharField(default="LH438"),
    "carrierCode": fields.CharField(default="LH"),
    "carrier": fields.CharField(default="LUFTHANSA"),
    "duration": fields.IntegerField(default=670),
    "aircraft": fields.CharField(default="AIRBUS A330-300"),
    "cabin": fields.ListField(child=copy(travel_classes)),
    "classId": fields.CharField(default="Y"),
})

itinerary = inline_serializer(name="Itinerary (Details)", fields={
    "duration": fields.IntegerField(default=670),
    "segments": fields.ListField(child=copy(segment)),
})

offer_details_response_schema = inline_serializer(name="OfferDetailsResponse", fields={
    "price": copy(price),
    "itineraries": fields.ListField(child=copy(itinerary)),
})
