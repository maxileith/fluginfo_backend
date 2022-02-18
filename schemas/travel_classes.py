from rest_framework import fields

travel_classes = fields.ChoiceField(
    choices=["ECONOMY", "FIRST", "BUSINESS", "PREMIUM_ECONOMY"], default="ECONOMY")
