from django.db import models


class Car_datasets(models.Model):
    document_id = models.IntegerField(primary_key=True)
    price = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    title_status = models.CharField(max_length=30)
    mileage = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    vin = models.CharField(max_length=30)
    lot = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    condition = models.CharField(max_length=30)

    def __str__(self):
        return self.brand
