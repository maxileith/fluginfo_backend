from rest_framework import fields
from drf_spectacular.utils import inline_serializer

price = inline_serializer(name="Price", fields={
    "value": fields.IntegerField(default=1234.56),
    "currency": fields.CharField(default="EURO"),
})
