from django.db import models


class Warehouse(models.Model):
    name = models.CharField('Наименование склада', max_length=64, db_index=True)
    address = models.CharField('Адрес', max_length=150, null=False)
    description = models.CharField('Описание', max_length=150, null=True, blank=True)
    useful_value = models.FloatField('Площадь', null=False)

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


class StorageType(models.Model):
    name = models.CharField('Наименование типа хранения', max_length=64, db_index=True)
    description = models.CharField('Описание', max_length=150, null=True, blank=True)
    storage_value = models.FloatField('Вместимость')
    warehouse = models.ManyToManyField('Warehouse', related_name='storage_types')

    class Meta:
        verbose_name = 'Тип хранения'
        verbose_name_plural = 'Типы хранения'


class Cargo(models.Model):
    name = models.CharField('Наименование груза', max_length=64, db_index=True)
    description = models.CharField('Описание', max_length=150, null=True, blank=True)
    cargo_value = models.FloatField('Объем груза')
    cargo_weight = models.FloatField('Вес груза')
    storage_type = models.OneToOneField(StorageType, on_delete=models.CASCADE, primary_key=True)
    warehouse = models.ForeignKey(Warehouse, verbose_name='cargos', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'
