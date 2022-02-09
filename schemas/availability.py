from rest_framework import fields
from drf_spectacular.utils import inline_serializer
from .price import price
from .stop import stop
from .travel_classes import travel_classes
from copy import copy

available_seats = inline_serializer(name="AvailableSeats", fields={
    "classId": fields.CharField(default="Y"),
    "seats": fields.IntegerField(default=9),
})

availability_exact_response_schema = inline_serializer(name="StatusExactResponse", fields={
    "flightNumber": fields.CharField(default="LH438"),
    "carrierCode": fields.CharField(default="LH"),
    "carrier": fields.CharField(default="LUFTHANSA", required=False),
    "departure": copy(stop),
    "arrival": copy(stop),
    "duration": fields.IntegerField(default=670),
    "aircraft": fields.CharField(default="Airbus A330-300"),
    "availableSeats": fields.ListField(child=copy(available_seats)),
})
