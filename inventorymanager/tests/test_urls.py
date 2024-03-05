import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from inventorymanager.models import Product, Establishment


@pytest.fixture
def create_product():
    return Product.objects.create(
        name="Test Product",
        description="This is a test product",
        price=10.00,
        quantity_in_stock=100,
    )


@pytest.fixture
def create_establishment():
    return Establishment.objects.create(
        name="Test Establishment",
        description="This is a test establishment",
        locations="Test Location",
        opening_hours="9:00-5:00",
    )


@pytest.mark.django_db
def test_product_detail_url(create_product):
    client = APIClient()
    url = reverse("product-detail", kwargs={"pk": create_product.pk})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_establishment_detail_url(create_establishment):
    client = APIClient()
    url = reverse("establishment-detail", kwargs={"pk": create_establishment.pk})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_product_list_url():
    client = APIClient()
    url = reverse("product-list")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_establishment_list_url():
    client = APIClient()
    url = reverse("establishment-list")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
