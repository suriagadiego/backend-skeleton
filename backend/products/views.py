from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Supplier, JobRole, PartNo, Product, TransactionHistory, Warehouse, Brand, Unit
from .serializers import (
    SupplierSerializer,
    UserSerializer, 
    JobRoleSerializer,
    PartNoSerializer,
    ProductSerializer,
    TransactionHistorySerializer,
    WarehouseSerializer,
    BrandSerializer,
    UnitSerializer,
    SupplierSerializer
)

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SupplierView(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class JobRoleView(viewsets.ModelViewSet):
    queryset = JobRole.objects.all()
    serializer_class = JobRoleSerializer

class PartNoView(viewsets.ModelViewSet):
    queryset = PartNo.objects.all()
    serializer_class = PartNoSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class TransactionHistoryView(viewsets.ModelViewSet):
    queryset = TransactionHistory.objects.all()
    serializer_class = TransactionHistorySerializer

class WarehouseView(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class UnitView(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

