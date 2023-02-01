from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    release_date = models.DateField(max_length=50)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)