from rest_framework import fields
from drf_spectacular.utils import inline_serializer
from copy import copy

airport = inline_serializer(name="Airport", fields={
    "iata": fields.CharField(default="FRA"),
    "name": fields.CharField(required=False, default="FRANFURT INTL"),
    "city": fields.CharField(required=False, default="FRANKFURT"),
    "countryCode": fields.CharField(required=False, default="DE"),
    "country": fields.CharField(required=False, default="GERMANY"),
    "timezone": fields.CharField(required=False, default="+01:00"),
})

airport_search_response_schema = inline_serializer(name="AirportSearchResponse", fields={
    "data": fields.ListField(child=copy(airport)),
})
