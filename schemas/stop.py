from rest_framework import fields
from drf_spectacular.utils import inline_serializer
from .airport import airport

stop = inline_serializer(name="Stop", fields={
    "airport": airport,
    "at": fields.CharField(default="2022-03-01T10:50:00"),
})
