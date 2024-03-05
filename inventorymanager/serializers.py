import re

from drf_spectacular.utils import (
    extend_schema,
    extend_schema_serializer,
    OpenApiExample,
)
from rest_framework import serializers
from .models import Product, Establishment


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "quantity_in_stock"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Valid Establishment Example",
            summary="Example of a valid establishment",
            description="A valid establishment with name, description, and opening hours.",
            value={
                "id": 1,
                "name": "Example Establishment",
                "description": "This is a sample establishment.",
                "locations": "Some location",
                "opening_hours": "09:00-17:00",
            },
            request_only=True,
        ),
        OpenApiExample(
            "Invalid Establishment Example",
            summary="Example of an invalid establishment",
            description="Opening hours must be in the format 'HH:MM-HH:MM'",
            value={
                "name": "Invalid Establishment",
                "description": "Description of establishment",
                "locations": "Some location",
                "opening_hours": "09:90-17:00",
            },
            request_only=True,
        ),
    ]
)
class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = ["id", "name", "description", "locations", "opening_hours"]

    def validate_opening_hours(self, value):
        pattern = r"^\d{1,2}:\d{2}-\d{1,2}:\d{2}$"

        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Opening hours must be in the format 'HH:MM-HH:MM'"
            )

        return value
