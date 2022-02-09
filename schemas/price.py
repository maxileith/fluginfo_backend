from rest_framework import fields
from drf_spectacular.utils import inline_serializer

price = inline_serializer(name="Price", fields={
    "value": fields.FloatField(help_text="e.g. 1234.56"),
    "currency": fields.CharField(help_text="e.g. EURO"),
})
