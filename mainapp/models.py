from django.db import models
# from slugify import slugify

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=255)
    # slug = models.SlugField(max_length=100, unique=True, blank=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Shop, self).save(*args, **kwargs)


class User(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    distance = models.FloatField()