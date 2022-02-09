from rest_framework import fields
from drf_spectacular.utils import inline_serializer

status_timings_response_schema = inline_serializer(name="StatusTimingsResponse", fields={
    "departure": fields.CharField(help_text="e.g. 2022-03-01T09:55"),
    "arrival": fields.CharField(help_text="e.g. 2022-03-01T14:15"),
})
