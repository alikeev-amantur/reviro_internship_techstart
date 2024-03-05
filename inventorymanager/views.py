from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from .models import Product, Establishment
from .serializers import ProductSerializer, EstablishmentSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer


class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all().order_by("id")
    serializer_class = EstablishmentSerializer
