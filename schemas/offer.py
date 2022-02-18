from rest_framework import fields
from drf_spectacular.utils import inline_serializer
from .stop import stop
from .travel_classes import travel_classes
from copy import copy

carrier = inline_serializer(name="Carrier", fields={
    "carrierCode": fields.CharField(help_text="e.g. FINNAIR"),
    "carrier": fields.CharField(help_text="e.g. AY"),
})

itinerary = inline_serializer(name="Itinerary", fields={
    "duration": fields.IntegerField(help_text="e.g. 670"),
    "stops": fields.IntegerField(help_text="e.g. 0"),
    "carriers": fields.ListField(child=copy(carrier)),
    "departure": copy(stop),
    "arrival": copy(stop),
    "classes": fields.ListField(child=copy(travel_classes)),
})

offer = inline_serializer(name="Offer", fields={
    "hash": fields.CharField(help_text="e.g. 719a854bc4d7d275e40419bbdb840dbea183ba80af26b554e7966c3d2146f26659c14c103663313970c0c58fc62db90d0e2ff38a68087fe4f167c39890825f76"),
    "price": fields.FloatField(help_text="e.g. 632.10"),
    "itineraries": fields.ListField(child=copy(itinerary)),
})

offer_search_response_schema = inline_serializer(name="OfferSearchResponse", fields={
    "data": fields.ListField(child=copy(offer)),
})
