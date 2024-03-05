import pytest
from django.core.exceptions import ValidationError
from rest_framework import serializers

from inventorymanager.serializers import EstablishmentSerializer, ProductSerializer


@pytest.mark.django_db
class TestProductSerializer:
    def test_valid_data(self):
        data = {
            "name": "Test Product",
            "description": "This is a test product",
            "price": "10.00",
            "quantity_in_stock": 100,
        }
        serializer = ProductSerializer(data=data)
        assert serializer.is_valid()
        assert "id" not in serializer.validated_data

    def test_invalid_name(self):
        invalid_data = {
            "name": "",
            "description": "This is a test product",
            "price": "10.00",
            "quantity_in_stock": 100,
        }
        serializer = ProductSerializer(data=invalid_data)
        assert not serializer.is_valid()
        assert "name" in serializer.errors

    def test_max_length_name(self):
        serializer = ProductSerializer(
            data={
                "name": "a" * 256,
                "description": "Test Description",
                "price": "10.00",
                "quantity_in_stock": 5,
            }
        )
        assert not serializer.is_valid()
        assert "name" in serializer.errors


@pytest.mark.django_db
class TestEstablishmentSerializer:
    def test_valid_data(self):
        data = {
            "name": "Test Establishment",
            "description": "This is a test establishment",
            "locations": "Test Location",
            "opening_hours": "9:00-17:00",
        }
        serializer = EstablishmentSerializer(data=data)
        assert serializer.is_valid()
        assert "id" not in serializer.validated_data

    def test_invalid_name(self):
        invalid_data = {
            "name": "",
            "description": "This is a test establishment",
            "locations": "Test Location",
            "opening_hours": "9:00-17:00",
        }
        serializer = EstablishmentSerializer(data=invalid_data)
        assert not serializer.is_valid()
        assert "name" in serializer.errors

    def test_invalid_opening_hours(self):
        invalid_data = {
            "name": "Test Establishment",
            "description": "Test description",
            "locations": "Test location",
            "opening_hours": "18:99-20:8s9",
        }
        serializer = EstablishmentSerializer(data=invalid_data)
        assert not serializer.is_valid()
        assert "opening_hours" in serializer.errors

    def test_max_length_name(self):
        serializer = EstablishmentSerializer(
            data={
                "name": "a" * 256,
                "description": "Test Description",
                "locations": "Test Location",
                "opening_hours": "09:00-17:00",
            }
        )
        assert not serializer.is_valid()
        assert "name" in serializer.errors

    def test_max_length_locations(self):
        serializer = EstablishmentSerializer(
            data={
                "name": "Test Name",
                "description": "Test Description",
                "locations": "a" * 256,
                "opening_hours": "09:00-17:00",
            }
        )
        assert not serializer.is_valid()
        assert "locations" in serializer.errors
