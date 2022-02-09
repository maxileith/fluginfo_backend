from rest_framework import fields
from drf_spectacular.utils import inline_serializer
from copy import copy

amenities_power = inline_serializer(name="AmenitiesPower", fields={
    "isChargeable": fields.BooleanField(help_text="e.g. false"),
    "type": fields.ChoiceField(choices=["Plug", "USB-Port", "Adaptor", "Plug or USB-Port"], help_text="e.g. USB-Port"),
})

amenities_seat_image = inline_serializer(name="AmenitiesSeatImage", fields={
    "title": fields.CharField(help_text="e.g. Comfortable Seats"),
    "href": fields.URLField(help_text="e.g. https://pdt.content.amadeus.com/AncillaryServicesMedia/14223418_395.jpg"),
    "description": fields.CharField(help_text=r"Settle in with comfortable seats and an ecoTHREAD blanket made from 100% recycled plastic bottles."),
})

amenities_seat = inline_serializer(name="AmenitiesSeat", fields={
    "legSpace": fields.CharField(help_text="e.g. 74 cm"),
    "tilt": fields.ChoiceField(choices=["Full flat", "Angled flat", "Normal"], help_text="e.g. Normal"),
    "images": fields.ListField(child=copy(amenities_seat_image)),
})

amenities_wifi = inline_serializer(name="AmenitiesWifi", fields={
    "isChargeable": fields.BooleanField(help_text="e.g. true"),
    "type": fields.ChoiceField(choices=["Full", "Partial"], help_text="e.g. Full"),
})

amenities_entertainment = inline_serializer(name="AmenitiesEntertainment", fields={
    "isChargeable": fields.BooleanField(help_text="e.g. false"),
    "type": fields.ChoiceField(choices=["Live-TV", "Movies", "Audio & Video on demand", "TV-Shows", "IP-TV"], help_text="e.g. Movies"),
})

amenities_food = inline_serializer(name="AmenitiesFood", fields={
    "isChargeable": fields.BooleanField(help_text="e.g. true"),
    "type": fields.ChoiceField(choices=["Meal", "Fresh meal", "Snacks", "Fresh snacks"], help_text="e.g. Snacks"),
})

amenities_beverage = inline_serializer(name="AmenitiesBeverage", fields={
    "isChargeable": fields.BooleanField(help_text="e.g. true"),
    "type": fields.ChoiceField(choices=["Alcoholic", "Non-Alcoholic", "With and without alcohol"], help_text="e.g. Snacks"),
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
    "start": fields.IntegerField(help_text="e.g. 0"),
    "end": fields.IntegerField(help_text="e.g. 9"),
})

deck_grid_item = inline_serializer(name="GridItemSeat", fields={
    "type": fields.ChoiceField(choices=["seat", "facility"], help_text="e.g. seat"),
    "number": fields.CharField(help_text="e.g. 12B (seat only)", required=False),
    "available": fields.BooleanField(help_text="e.g. true (seat only)", required=False),
    "characteristics": fields.ListField(child=fields.CharField(help_text="e.g. No infants. (seat only)"), required=False),
    "name": fields.CharField(help_text="e.g. Galley (facility only)", required=False),
})

deck = inline_serializer(name="Deck", fields={
    "wingsX": copy(deck_wings_x),
    "exitRowsX": fields.ListField(child=fields.IntegerField(help_text="e.g. 42"), required=False),
    "grid": fields.ListField(child=fields.ListField(child=copy(deck_grid_item))),
})

seatmap_response_schema = inline_serializer(name="SeatmapResponse", fields={
    "flightNumber": fields.CharField(help_text="e.g. LH438"),
    "classId": fields.CharField(help_text="e.g. Y"),
    "departureIata": fields.CharField(help_text="e.g. FRA"),
    "arrivalIata": fields.CharField(help_text="e.g. DFW"),
    "date": fields.CharField(help_text="e.g. 2022-03-01"),
    "amenities": copy(amenities),
    "decks": fields.ListField(child=copy(deck)),
})
