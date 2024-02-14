from django.urls import path
from . import views

app_name = "warehouses"

urlpatterns = [
    path(
        "warehouse_list/",
        views.WarehouseListView.as_view(),
        name="warehouse_list",
    ),
    path(
        "storagetype_list/",
        views.StorageTypeListView.as_view(),
        name="storagetype_list",
    ),
    path(
        "cargo_list/",
        views.CargoListView.as_view(),
        name="cargo_list",
    ),
    path(
        "warehouse_detail/<int:pk>/",
        views.WarehouseDetailView.as_view(),
        name="warehouse_detail",
    ),
    path(
        "storagetype_detail/<int:pk>/",
        views.StorageTypeDetailView.as_view(),
        name="storagetype_detail",
    ),
    path(
        "cargo_detail/<int:pk>/",
        views.CargoDetailView.as_view(),
        name="cargo_detail",
    ),
]