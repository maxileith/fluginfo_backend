from rest_framework import fields
from drf_spectacular.utils import inline_serializer
from .price import price
from .stop import stop
from .travel_classes import travel_classes
from copy import copy

available_seats = inline_serializer(name="AvailableSeats", fields={
    "classId": fields.CharField(help_text="e.g. Y"),
    "seats": fields.IntegerField(default=9),
})

status_exact_response_schema = inline_serializer(name="StatusExactResponse", fields={
    "flightNumber": fields.CharField(help_text="e.g. LH438"),
    "carrierCode": fields.CharField(help_text="e.g. LH"),
    "carrier": fields.CharField(help_text="e.g. LUFTHANSA", required=False),
    "departure": copy(stop),
    "arrival": copy(stop),
    "duration": fields.IntegerField(help_text="e.g. 670"),
    "aircraft": fields.CharField(help_text="e.g. Airbus A330-300"),
    "availableSeats": fields.ListField(child=copy(available_seats)),
})
