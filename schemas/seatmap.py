from rest_framework import fields
from drf_spectacular.utils import inline_serializer
from .price import price
from .stop import stop
from .travel_classes import travel_classes
from copy import copy

amenities_power = inline_serializer(name="AmenitiesPower", fields={
    "isChargeable": fields.BooleanField(default=False),
    "type": fields.ChoiceField(choices=["Plug", "USB-Port", "Adaptor", "Plug or USB-Port"], default="USB-Port"),
})

amenities_seat_image = inline_serializer(name="AmenitiesSeatImage", fields={
    "title": fields.CharField(default="Comfortable Seats"),
    "href": fields.URLField(default="https://pdt.content.amadeus.com/AncillaryServicesMedia/14223418_395.jpg"),
    "description": fields.CharField(default=r"Settle in with comfortable seats and an ecoTHREAD blanket made from 100% recycled plastic bottles."),
})

amenities_seat = inline_serializer(name="AmenitiesSeat", fields={
    "legSpace": fields.CharField(default="74 cm"),
    "tilt": fields.ChoiceField(choices=["Full flat", "Angled flat", "Normal"], default="Normal"),
    "images": fields.ListField(child=copy(amenities_seat_image)),
})

amenities_wifi = inline_serializer(name="AmenitiesWifi", fields={
    "isChargeable": fields.BooleanField(default=True),
    "type": fields.ChoiceField(choices=["Full", "Partial"], default="Full"),
})

amenities_entertainment = inline_serializer(name="AmenitiesEntertainment", fields={
    "isChargeable": fields.BooleanField(default=False),
    "type": fields.ChoiceField(choices=["Live-TV", "Movies", "Audio & Video on demand", "TV-Shows", "IP-TV"], default="Movies"),
})

amenities_food = inline_serializer(name="AmenitiesFood", fields={
    "isChargeable": fields.BooleanField(default=True),
    "type": fields.ChoiceField(choices=["Meal", "Fresh meal", "Snacks", "Fresh snacks"], default="Snacks"),
})

amenities_beverage = inline_serializer(name="AmenitiesBeverage", fields={
    "isChargeable": fields.BooleanField(default=True),
    "type": fields.ChoiceField(choices=["Alcoholic", "Non-Alcoholic", "With and without alcohol"], default="Snacks"),
})

amenities = inline_serializer(name="Amenities", fields={
    "power": copy(amenities_power),
    "seat": copy(amenities_seat),
    "wifi": copy(amenities_wifi),
    "entertainment": copy(amenities_entertainment),
    "food": copy(amenities_food),
    "beverage": copy(amenities_beverage),
})

deck_wings_x = inline_serializer(name="DeckWingsX", fields={
    "start": fields.IntegerField(default=0),
    "end": fields.IntegerField(default=9),
})

deck_seat_rows = inline_serializer(name="DeckSeatRows", fields={
    "start": fields.IntegerField(default=10),
    "end": fields.IntegerField(default=31),
})

deck_grid_seat = inline_serializer(name="GridSeat", fields={
    "type": fields.ChoiceField(choices=["seat"], default="seat"),
    "number": fields.CharField(default="12B"),
    "available": fields.BooleanField(default=True),
    "characteristics": fields.ListField(child=fields.CharField(default="No infants."), required=False),
})

deck_grid_facility = inline_serializer(name="GridFacility", fields={
    "type": fields.ChoiceField(choices=["facility"], default="facility"),
    "name": fields.CharField(default="Galley"),
})

deck = inline_serializer(name="Deck", fields={
    "wingsX": copy(deck_wings_x),
    "seatRows": copy(deck_seat_rows),
    "exitRowsX": fields.ListField(child=fields.IntegerField(default=42), required=False),
    "grid": fields.ListField(child=fields.ListField(child=copy(deck_grid_seat))),
})

seatmap_response_schema = inline_serializer(name="SeatmapResponse", fields={
    "flightNumber": fields.CharField(default="LH438"),
    "classId": fields.CharField(default="Y"),
    "departureIata": fields.CharField(default="FRA"),
    "arrivalIata": fields.CharField(default="DFW"),
    "date": fields.CharField(default="2022-03-01"),
    "amenities": copy(amenities),
    "decks": fields.ListField(child=deck),
})
