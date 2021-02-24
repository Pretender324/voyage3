from django.db import models
from django.utils import timezone

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    making_time = models.CharField(max_length=100, null=False, blank=False)
    serves = models.CharField(max_length=100, null=False, blank=False)
    ingredients = models.CharField(max_length=300, null=False, blank=False)
    cost = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
