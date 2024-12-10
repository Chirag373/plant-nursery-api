from django.db import models
from django.core.exceptions import ValidationError

GROWTH_STAGE = [
    ("seed", "Seed"),
    ("seedling", "Seedling"),
    ("young", "young"),
    ("mature", "mature"),
]

# Create your models here.
class Plant(models.Model):
    species = models.CharField(
        max_length=100, 
        blank=False, 
        null=False
    )
    planting_date = models.DateTimeField(auto_now_add=True)
    last_watered_date = models.DateTimeField(auto_now_add=True)
    health = models.IntegerField()
    growth_stage = models.CharField(
        max_length=20, 
        choices=GROWTH_STAGE, 
        blank=False, 
        null=False
    )

    def __str__(self):
        return self.species