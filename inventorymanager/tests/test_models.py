import pytest

from inventorymanager.models import Product, Establishment


@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        name="Test Product",
        description="This is a test product",
        price=10.00,
        quantity_in_stock=100,
    )
    assert Product.objects.count() == 1
    assert product.name == "Test Product"
    assert product.description == "This is a test product"
    assert product.price == 10.00
    assert product.quantity_in_stock == 100


@pytest.mark.django_db
def test_create_establishment():
    establishment = Establishment.objects.create(
        name="Test Establishment",
        description="This is a test establishment",
        locations="Test Location",
        opening_hours="9:00-5:00",
    )
    assert Establishment.objects.count() == 1
    assert establishment.name == "Test Establishment"
    assert establishment.description == "This is a test establishment"
    assert establishment.locations == "Test Location"
    assert establishment.opening_hours == "9:00-5:00"


@pytest.mark.django_db
def test_product_name_max_length():
    max_length = Product._meta.get_field("name").max_length
    assert max_length == 255


@pytest.mark.django_db
def test_establishment_name_max_length():
    max_length = Establishment._meta.get_field("name").max_length
    assert max_length == 255


@pytest.mark.django_db
def test_establishment_locations_max_length():
    max_length = Establishment._meta.get_field("locations").max_length
    assert max_length == 255


@pytest.mark.django_db
def test_product_field_types():
    # Creating a test product
    product = Product.objects.create(
        name="Test Product",
        description="This is a test product",
        price=10.00,
        quantity_in_stock=100,
    )
    assert isinstance(product.quantity_in_stock, int)


@pytest.mark.django_db
def test_establishment_field_types():
    establishment = Establishment.objects.create(
        name="Test Establishment",
        description="This is a test establishment",
        locations="Test Location",
        opening_hours="9:00-5:00",
    )
    assert isinstance(establishment.opening_hours, str)
