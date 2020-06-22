class BlogIndex(DocType):
    document_id = Integer()


    document_id = models.IntegerField(primary_key=True)
    price = Text()
    brand = Text()
    model = Text()
    year = Text()
    title_status = Text()
    mileage = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    vin = models.CharField(max_length=30)
    lot = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    condition = models.CharField(max_length=30)