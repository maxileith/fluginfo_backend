from rest_framework import fields
from drf_spectacular.utils import inline_serializer
from .airport import airport
from copy import copy

stop = inline_serializer(name="Stop", fields={
    "airport": copy(airport),
    "at": fields.CharField(help_text="e.g. 2022-03-01T10:50:00"),
})
