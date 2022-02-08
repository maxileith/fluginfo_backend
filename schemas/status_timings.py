from rest_framework import fields
from drf_spectacular.utils import inline_serializer

status_timings_response_schema = inline_serializer(name="StatusTimingsResponse", fields={
    "departure": fields.CharField(default="2022-03-01T09:55"),
    "arrival": fields.CharField(default="2022-03-01T14:15"),
})
