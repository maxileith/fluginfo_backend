from rest_framework import fields
from drf_spectacular.utils import inline_serializer
from .price import price
from .stop import stop
from .travel_classes import travel_classes
from copy import copy

carrier = inline_serializer(name="Carrier", fields={
    "carrierCode": fields.CharField(default="FINNAIR"),
    "carrier": fields.CharField(default="AY"),
})

itinerary = inline_serializer(name="Itinerary", fields={
    "duration": fields.IntegerField(default=670),
    "stops": fields.IntegerField(default=0),
    "carriers": fields.ListField(child=copy(carrier)),
    "departure": copy(stop),
    "arrival": copy(stop),
    "classes": fields.ListField(child=copy(travel_classes)),
})

offer = inline_serializer(name="Offer", fields={
    "hash": fields.CharField(default="719a854bc4d7d275e40419bbdb840dbea183ba80af26b554e7966c3d2146f26659c14c103663313970c0c58fc62db90d0e2ff38a68087fe4f167c39890825f76"),
    "price": copy(price),
    "itineraries": fields.ListField(child=copy(itinerary)),
})

offer_search_response_schema = inline_serializer(name="OfferSearchResponse", fields={
    "data": fields.ListField(child=copy(offer)),
})
