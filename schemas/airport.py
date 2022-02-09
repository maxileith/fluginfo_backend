from rest_framework import fields
from drf_spectacular.utils import inline_serializer
from copy import copy

airport = inline_serializer(name="Airport", fields={
    "iata": fields.CharField(help_text="e.g. FRA"),
    "name": fields.CharField(required=False, help_text="e.g. FRANFURT INTL"),
    "city": fields.CharField(required=False, help_text="e.g. FRANKFURT"),
    "countryCode": fields.CharField(required=False, help_text="e.g. DE"),
    "country": fields.CharField(required=False, help_text="e.g. GERMANY"),
    "timezone": fields.CharField(required=False, help_text="e.g. +01:00"),
})

airport_search_response_schema = inline_serializer(name="AirportSearchResponse", fields={
    "data": fields.ListField(child=copy(airport)),
})
