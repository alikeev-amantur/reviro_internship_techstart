import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from inventorymanager.models import Product, Establishment


@pytest.mark.django_db
def test_product_viewset_list():
    client = APIClient()
    url = reverse("product-list")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_product_viewset_create():
    client = APIClient()
    url = reverse("product-list")
    data = {
        "name": "Test Product",
        "description": "This is a test product",
        "price": "10.00",
        "quantity_in_stock": 100,
    }
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Product.objects.count() == 1
    assert Product.objects.get().name == "Test Product"


@pytest.mark.django_db
def test_establishment_viewset_list():
    client = APIClient()
    url = reverse("establishment-list")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_establishment_viewset_create():
    client = APIClient()
    url = reverse("establishment-list")
    data = {
        "name": "Test Establishment",
        "description": "This is a test establishment",
        "locations": "Test Location",
        "opening_hours": "9:00-17:00",
    }
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Establishment.objects.count() == 1
    assert Establishment.objects.get().name == "Test Establishment"
