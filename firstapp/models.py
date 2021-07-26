from django.db import models

# Create your models here.
class register(models.Model):
    name = models.CharField(max_length=120, null=False)
    reason = models.CharField(max_length=120, null=False)
    time = models.DateTimeField()


class ProductModel(models.Model):
    name = models.CharField(max_length=120, null=False)
    price = models.PositiveIntegerField(null=False)
    seller = models.CharField(max_length=120, null=False)
    category = models.CharField(max_length=120, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
