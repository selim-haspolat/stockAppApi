from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# ---------------------------------
# FixView
# ---------------------------------
class FixView(ModelViewSet):
    filter_backends = [SearchFilter, DjangoFilterBackend]
    # permission_classes = [DjangoModelPermissions]

# ---------------------------------
# Views
# ---------------------------------
from .serializers import (
    Category, CategorySerializer,
    Brand, BrandSerializer,
    Product, ProductSerializer,
    Firm, FirmSerializer,
    Purchase, PurchaseSerializer,
    Sale, SaleSerializer,
)


class CategoryView(FixView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['name']


class BrandView(FixView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    search_fields = ['name']


class ProductView(FixView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name']
    filterset_fields = ['category', 'brand']


class FirmView(FixView):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    search_fields = ['name']


class PurchaseView(FixView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filterset_fields = ['firm', 'brand','product']


class SaleView(FixView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filterset_fields = ['brand','product']