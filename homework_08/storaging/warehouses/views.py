from .models import Warehouse, StorageType, Cargo
from django.views.generic import ListView, DetailView


class WarehouseListView(ListView):
    model = Warehouse


class WarehouseDetailView(DetailView):
    model = Warehouse


class StorageTypeListView(ListView):
    model = StorageType


class StorageTypeDetailView(DetailView):
    model = StorageType


class CargoListView(ListView):
    model = Cargo


class CargoDetailView(DetailView):
    model = Cargo
