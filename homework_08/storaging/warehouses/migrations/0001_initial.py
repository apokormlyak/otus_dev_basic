# Generated by Django 4.2.7 on 2023-12-26 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Warehouse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=64, verbose_name="Наименование склада"
                    ),
                ),
                ("address", models.CharField(max_length=150, verbose_name="Адрес")),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="Описание"
                    ),
                ),
                ("useful_value", models.FloatField(verbose_name="Площадь")),
            ],
            options={
                "verbose_name": "Склад",
                "verbose_name_plural": "Склады",
            },
        ),
        migrations.CreateModel(
            name="StorageType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        max_length=64,
                        verbose_name="Наименование типа хранения",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="Описание"
                    ),
                ),
                ("storage_value", models.FloatField(verbose_name="Вместимость")),
                (
                    "warehouse",
                    models.ManyToManyField(
                        related_name="storage_types", to="warehouses.warehouse"
                    ),
                ),
            ],
            options={
                "verbose_name": "Тип хранения",
                "verbose_name_plural": "Типы хранения",
            },
        ),
        migrations.CreateModel(
            name="Cargo",
            fields=[
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=64, verbose_name="Наименование груза"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="Описание"
                    ),
                ),
                ("cargo_value", models.FloatField(verbose_name="Объем груза")),
                ("cargo_weight", models.FloatField(verbose_name="Вес груза")),
                (
                    "storage_type",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="warehouses.storagetype",
                    ),
                ),
                (
                    "warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="warehouses.warehouse",
                        verbose_name="cargos",
                    ),
                ),
            ],
            options={
                "verbose_name": "Груз",
                "verbose_name_plural": "Грузы",
            },
        ),
    ]
