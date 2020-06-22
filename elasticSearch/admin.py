from django.contrib import admin
from .models import Car_datasets
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Car_datasets)
class Car(ImportExportModelAdmin):
    pass


