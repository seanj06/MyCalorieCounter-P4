from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import date

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=200, null=False)
    quantity = models.PositiveIntegerField(null=False, default=0)
    calories = models.FloatField(null=False, default=0)

    def __str__(self):
        return self.name


class FoodCategory(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Food Category'
        verbose_name_plural = 'Food Categories'

    def __str__(self):
        return f'{self.category_name}'